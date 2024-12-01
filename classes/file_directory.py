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
        self.file_dict = {}

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

    # ================ Normal Functions

    def read_file_list(self) -> None:
        """When the directory path is initialized, 
           read every file in the path and store them in a list."""
        # Checks to make sure directory is active.
        if not os.path.isdir(self.directory_path):
            raise InvalidDirectoryPath
        # Dict comprehension to read each file/folder in a directory
        # Key and value will be the same, value changed when prefixing and the like.
        self.file_dict = {file: file for file in os.listdir(self.directory_path)}