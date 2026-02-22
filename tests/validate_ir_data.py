import os
import unittest

class TestIRData(unittest.TestCase):
    """
    Test suite for validating the integrity and format of IR signal capture data files.

    This class provides a set of unit tests to ensure that all .ir files within the
    `data/ir_captures` directory adhere to the expected structure and content requirements.
    It verifies file existence and validates the format of raw data fields to prevent
    issues during playback on the Flipper Zero device.
    """

    def get_ir_files(self):
        """
        Recursively collects all .ir files from the project's IR captures directory.

        This helper method traverses the `data/ir_captures` directory tree to find
        all files with the `.ir` extension, which contain the infrared signal data.

        Returns:
            list: A list of absolute or relative file paths (strings) pointing to
                  each found .ir file.
        """
        ir_files = []
        ir_dir = 'data/ir_captures'
        for root, dirs, files in os.walk(ir_dir):
            for file in files:
                if file.endswith('.ir'):
                    ir_files.append(os.path.join(root, file))
        return ir_files

    def test_raw_data_is_integers(self):
        """
        Verifies that all signals of type 'raw' contain strictly integer values in their data field.

        This test iterates through every found .ir file and parses its content.
        For sections identified as `type: raw`, it checks the `data:` field to ensure:
        1.  The field is not empty.
        2.  Every value in the space-separated list is a valid integer.

        This validation is crucial because the Flipper Zero expects raw timing data
        (in microseconds) to be numeric. Non-integer values will cause playback failure.

        Raises:
            AssertionError: If no .ir files are found, if a data field is empty,
                            or if a non-integer value is encountered in a raw data block.
        """
        files = self.get_ir_files()
        self.assertTrue(len(files) > 0, "No .ir files found")

        for filepath in files:
            with self.subTest(filepath=filepath):
                with open(filepath, 'r') as f:
                    is_raw = False
                    for i, line in enumerate(f):
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
