import unittest
from functions.get_files_info import get_file_content


class TestGetFilesInfo(unittest.TestCase):
    def test_calculator_files(self):
        result = get_file_content("calculator", "main.py")
        print(result)
        # self.assertEqual(result, expected)

    def test_calculator_pkg_files(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        # self.assertEqual(result, expected)

    def test_calculator_bin(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)
        self.assertEqual(result, 'Error: File not found or is not a regular file: "/bin/cat"')

if __name__ == "__main__":
    unittest.main()
