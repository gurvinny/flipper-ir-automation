import os
import unittest
import re

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

    def test_filename_convention(self):
        """
        Verifies that IR files follow the naming convention: grvroom_<device>_<brand>.ir
        This convention applies to files outside the 'templates' directory.
        """
        files = self.get_ir_files()
        pattern = re.compile(r'^grvroom_[a-z]+_[a-z]+\.ir$')

        for filepath in files:
            # Skip templates directory
            if 'templates' in filepath:
                continue

            filename = os.path.basename(filepath)
            with self.subTest(filepath=filepath):
                self.assertTrue(pattern.match(filename),
                                f"File '{filename}' does not match naming convention 'grvroom_<device>_<brand>.ir'")

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

    def test_hex_pattern_redos(self):
        """
        Verifies that the hex_pattern regular expression is not vulnerable to
        Regular Expression Denial of Service (ReDoS) via catastrophic backtracking.
        """
        hex_pattern = re.compile(r'^([0-9A-Fa-f]{2}(?: [0-9A-Fa-f]{2})*)$')
        import time
        start = time.time()
        # Malicious payload: long string of valid parts followed by an invalid part
        payload = "00" + " 00" * 50000 + " a"
        hex_pattern.match(payload)
        duration = time.time() - start
        self.assertLess(duration, 0.5, "ReDoS detected: Hex regex evaluation took too long.")

    def test_parsed_data_fields(self):
        """
        Verifies that signals of type 'parsed' have valid protocol, address, and command fields.
        - Protocol: Alphanumeric string.
        - Address/Command: Space-separated 2-digit hex values.
        """
        files = self.get_ir_files()
        # Matches pairs of hex digits separated by spaces
        hex_pattern = re.compile(r'^([0-9A-Fa-f]{2}(?: [0-9A-Fa-f]{2})*)$')
        protocol_pattern = re.compile(r'^[a-zA-Z0-9]+$')

        for filepath in files:
            with self.subTest(filepath=filepath):
                with open(filepath, 'r') as f:
                    is_parsed = False
                    for i, line in enumerate(f):
                        line = line.strip()
                        if line.startswith('type: parsed'):
                            is_parsed = True
                        elif line.startswith('type: raw'):
                            is_parsed = False

                        if is_parsed:
                            if line.startswith('protocol:'):
                                content = line.split(':', 1)[1].strip()
                                self.assertTrue(protocol_pattern.match(content),
                                                f"Invalid protocol format in {filepath} line {i+1}: '{content}'")
                            elif line.startswith('address:') or line.startswith('command:'):
                                content = line.split(':', 1)[1].strip()
                                self.assertTrue(hex_pattern.match(content),
                                                f"Invalid hex format in {filepath} line {i+1}: '{content}'")

if __name__ == '__main__':
    unittest.main()
