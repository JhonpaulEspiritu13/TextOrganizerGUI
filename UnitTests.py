"""
* Name         : Unit Test (UnitTests.py)
* Author       : Jhon Paul Espiritu
* Created      : 11/30/2024
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : This demonstrates the use of unit testing.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

# Imports
import unittest
import os
# Classes
from classes.file_directory import FileDirectory
from classes.exceptions import *

# Ensure that this stays non-existent, used for testing non-folders.
NONEXISTENT_FOLDER_PATH = "never_before_seen_folder"

class FileDirectoryTestCase(unittest.TestCase):
    """Test cases for the FileDirectory class."""
    def setUp(self):
        """Sets up the test cases' directory."""
        # Current directory.
        self.test_directory = FileDirectory(os.getcwd())

    def tearDown(self):
        """Tears down the test cases' directory."""
        del self.test_directory

    def test_directory_raises_format_error(self):
        """Ensures that an error is raised when input is not string"""
        with self.assertRaises(InvalidDirectoryFormat):
            FileDirectory(1)

    def test_directory_raises_invalid_path_error(self):
        """Ensures that an error is raised when folder does not exist."""
        with self.assertRaises(InvalidDirectoryPath):
            FileDirectory(os.path.join(os.getcwd(), NONEXISTENT_FOLDER_PATH))

    def test_directory_raises_no_path_error(self):
        """Ensures that an error is raised when string is empty."""
        with self.assertRaises(NoDirectoryPath):
            FileDirectory("")

    def test_read_files_raises_invalid_path_error(self):
        """Ensures that an error is raised when folder does not exist. (read_file_list ver.)"""
        with self.assertRaises(InvalidDirectoryPath):
            # Creates a folder path for this specific test.
            new_folder_path = os.path.join(os.getcwd(), NONEXISTENT_FOLDER_PATH)
            os.makedirs(new_folder_path)
            # Creates a new directory object, then deletes the folder path so the path is invalid.
            test_directory2 = FileDirectory(new_folder_path)
            os.rmdir(new_folder_path)
            test_directory2.read_file_list()

if __name__ == "__main__":
    unittest.main()