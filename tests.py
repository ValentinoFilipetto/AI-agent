import unittest

from functions.run_python_file import run_python_file
from functions.write_file import write_file


class TestFunctions(unittest.TestCase):
    def test_calculator_files(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_calculator_pkg_files(self):
        result = write_file(
            "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
        )
        print(result)

    ## a path that starts with / like /tmp/temp.txt is outside the working directory
    ## In many operating systems, a path that starts with / indicates an absolute path, meaning it's relative to the root of the file system
    def test_calculator_bin(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertEqual(
            result,
            'Error: Cannot write "/tmp/temp.txt" as it is outside the permitted working directory',
        )

    def test_run_main(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_run_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_run_main_outside_wd(self):
        result = run_python_file("calculator", "../main.py")
        print(result)
        self.assertEqual(
            result,
            'Error: Cannot execute "../main.py" as it is outside the permitted working directory',
        )

    def test_run_main_error(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        self.assertEqual(result, 'Error: File "nonexistent.py" not found.')


if __name__ == "__main__":
    unittest.main()
