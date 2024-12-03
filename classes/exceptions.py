"""
* Name         : Exceptions (exceptions.py)
* Author       : Jhon Paul Espiritu
* Created      : 11/26/2024
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : Stores all the exceptions that may be raised in processing.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

class InvalidDirectoryFormat(Exception):
    """The given value is not a string."""
    pass

class InvalidDirectoryPath(Exception):
    """The current selected directory cannot be found/used."""
    pass

class NoDirectoryPath(Exception):
    """There is no directory path available."""
    pass

class MissingFileError(Exception):
    """A file was missing from the directory path."""
    pass