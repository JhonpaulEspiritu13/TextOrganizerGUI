"""
* Name         : File Directory (file_directory.py)
* Author       : Jhon Paul Espiritu
* Created      : 11/26/2024
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : Stores the file directory and its objects into a class.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

# Imports
import os
from classes.exceptions import *

class FileDirectory:
    """File Directory class that stores file information and structure."""

    def __init__(self, file_path: str):
        """Creates a new FIleDirectory object.
        
        :param file_path: str - Directory path used to determine all files in a folder."""
        self.directory_path = file_path
        self.directory_list = []
        self.file_list = []

    # ================ Properties

    @property
    def directory_path(self):
        """Directory path referenced for files."""
        return self._directory_path
    
    @directory_path.setter
    def directory_path(self, value: str):
        """Sets the directory name.
        
        :param value: str - Directory path used to determine all files in a folder."""
        # Ensures that the directory path is a string.
        if not isinstance(value, str):
            raise InvalidDirectoryFormat
        # Ensures that the directory path is not empty.
        if not value:
            raise NoDirectoryPath
        # Checks to make sure directory is active.
        if not os.path.isdir(value):
            raise InvalidDirectoryPath
        self._directory_path = value

    # ================ Private Functions

    def _error_check(self, errors) -> None:
        """Handle error checking, where "ignore" passes while "raise" causes an error.
        
        :param errors: The option to check the error."""
        # CONSTANTS
        IGNORE = "ignore"
        RAISE = "raise"

        if errors == IGNORE:
            return
        elif errors == RAISE:
            raise MissingFileError
        else:
            raise ValueError

    # ================ Normal Functions

    def read_file_list(self) -> None:
        """When the directory path is initialized, 
           read every file in the path and store them in a list."""
        # Checks to make sure directory is active.
        if not os.path.isdir(self.directory_path):
            raise InvalidDirectoryPath
        read_list = os.listdir(self.directory_path)
        # List comprehension to read each file/folder in a directory
        # Key and value will be the same, value changed when prefixing and the like.
        self.file_dict = [file for file in read_list if os.path.isfile(os.path.join(self.directory_path, file))]
        self.directory_dict = [folder for folder in read_list if os.path.isdir(os.path.join(self.directory_path, folder))]

    def get_file_values(self, errors = "raise"):
        """Gets the file list values.
           
           :param errors: Default to raise. "ignore" passes missing files. "raise" causes error.
           :return: A list containing file values"""
        # Return Lists
        files = []

        # Iterate through dictionary
        for file in self.file_dict:
            # File path to check
            path = os.path.join(self.directory_path, file)
            # If file path is file, append it to list.
            if os.path.isfile(path):
                files.append(file)
            # File was not found
            else:
                self._error_check(errors)

        return files
    
    def get_directory_values(self, errors = "raise"):
        """Gets the folder list values.
           
           :param errors: Default to raise. "ignore" passes missing files. "raise" causes error.
           :return: A list containing file values"""
        # Return Lists
        folders = []

        # Iterate through dictionary
        for folder in self.directory_dict:
            # File path to check
            path = os.path.join(self.directory_path, folder)
            # If file path is file, append it to list.
            if os.path.isdir(path):
                folders.append(folder)
            # File was not found
            else:
                self._error_check(errors)

        return folders