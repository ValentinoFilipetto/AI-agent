import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_calculator_files(self):
        expected = (
            "tests.py: file_size=1342, is_dir=False\n"
            "main.py: file_size=564, is_dir=False\n"
            "pkg: file_size=4096, is_dir=True\n"
        )
        result = get_files_info("calculator", ".")
        print(result)
        self.assertEqual(result, expected)

    def test_calculator_pkg_files(self):
        expected = (
            "render.py: file_size=753, is_dir=False\n"
            "calculator.py: file_size=1720, is_dir=False\n"
            "__pycache__: file_size=4096, is_dir=True\n"
        )
        result = get_files_info("calculator", "pkg")
        print(result)
        self.assertEqual(result, expected)

    def test_calculator_bin(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    def test_calculator_baxk(self):
        result = get_files_info("calculator", "../")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')


if __name__ == "__main__":
    unittest.main()
