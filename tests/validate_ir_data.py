import os
import unittest

class TestIRData(unittest.TestCase):
    def get_ir_files(self):
        ir_files = []
        ir_dir = 'data/ir_captures'
        for root, dirs, files in os.walk(ir_dir):
            for file in files:
                if file.endswith('.ir'):
                    ir_files.append(os.path.join(root, file))
        return ir_files

    def test_raw_data_is_integers(self):
        files = self.get_ir_files()
        self.assertTrue(len(files) > 0, "No .ir files found")

        for filepath in files:
            with self.subTest(filepath=filepath):
                with open(filepath, 'r') as f:
                    lines = f.readlines()

                is_raw = False
                for i, line in enumerate(lines):
                    line = line.strip()
                    if line.startswith('type: raw'):
                        is_raw = True
                    elif line.startswith('type: parsed'):
                        is_raw = False

                    if line.startswith('data:'):
                        if is_raw:
                            data_content = line.replace('data:', '').strip()
                            self.assertTrue(len(data_content) > 0, f"Empty data field at line {i+1} in {filepath}")

                            values = data_content.split()
                            for val in values:
                                try:
                                    int(val)
                                except ValueError:
                                    self.fail(f"Non-integer value '{val}' found in data field at line {i+1} in {filepath}")
                        # If it's not raw, we don't strictly require data: to be integers,
                        # but usually parsed signals don't have a 'data:' field,
                        # they have 'address:' and 'command:'.

if __name__ == '__main__':
    unittest.main()
