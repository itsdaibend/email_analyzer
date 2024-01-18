import unittest
import subprocess


class TestScript(unittest.TestCase):
    def test_valid_input(self):
        subprocess.run(
            [
                "python",
                "script.py",
                "--input",
                "valid_input.jpg",
                "--output",
                "output.txt",
            ],
            capture_output=True,
            text=True,
        )
        expected_output, actual_output = "admin@hubspot.com", ""
        with open("output.txt", "r") as output_file:
            for email in output_file:
                actual_output += email.strip()
        self.assertEqual(
            actual_output,
            expected_output,
            f"Expected output: {expected_output}, Actual output: {actual_output}",
        )

    def test_invalid_input(self):
        result = subprocess.run(
            [
                "python",
                "script.py",
                "--input",
                "invalid_input.jpg",
                "--output",
                "output.txt",
            ],
            capture_output=True,
            text=True,
        )
        self.assertIn(
            f"CV2 returned a None object. Please, enter a valid path. "
            f"Use argument --input <path/to/file.txt>",
            result.stderr,
        )


if __name__ == "__main__":
    unittest.main()
