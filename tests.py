import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_calculator_files(self):
        expected = (
            "main.py: file_size=587, is dir=False\n"
            "pkg: file_size=0, is dir=True\n"
            "tests.py: file_size=1390, is dir=False\n"
        )
        result = get_files_info("calculator", ".")
        self.assertEqual(result, expected)

    def test_calculator_pkg_files(self):
        expected = (
            "calculator.py: file_size=1778, is dir=False\n"
            "render.py: file_size=773, is dir=False\n"
            "__pycache__: file_size=0, is dir=True\n"
        )
        result = get_files_info("calculator", "pkg")
        self.assertEqual(result, expected)

    def test_calculator_bin(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    def test_calculator_baxk(self):
        result = get_files_info("calculator", "../")
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')


if __name__ == "__main__":
    unittest.main()