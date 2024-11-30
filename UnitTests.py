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
        self.test_directory = os.getcwd()

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

if __name__ == "__main__":
    unittest.main()