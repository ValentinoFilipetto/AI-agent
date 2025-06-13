import unittest
from functions.get_files_info import write_file


class TestGetFilesInfo(unittest.TestCase):
    def test_calculator_files(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)

    def test_calculator_pkg_files(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)

    ## a path that starts with / like /tmp/temp.txt is outside the working directory
    ## In many operating systems, a path that starts with / indicates an absolute path, meaning it's relative to the root of the file system
    def test_calculator_bin(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertEqual(result, 'Error: Cannot write "/tmp/temp.txt" as it is outside the permitted working directory')

if __name__ == "__main__":
    unittest.main()
