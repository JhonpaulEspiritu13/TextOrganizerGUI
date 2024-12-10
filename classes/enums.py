"""
* Name         : Enums (enums.py)
* Author       : Jhon Paul Espiritu
* Created      : 11/26/2024
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : Stores the enumerations used for different names.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

from enum import Enum

class PrefixMode(Enum):
    """Prefix Enum that identifies the mode used to apply prefixes to folders."""
    ALPHANUMERIC = 0
    NUMERIC = 1
    CUSTOM = 2

class PrefixName(Enum):
    """Prefix Enum that identifies the name for the modes."""
    ALPHANUMERIC = "Alpha"
    NUMERIC = "Numeric"
    CUSTOM = "Custom"

class PrefixBase(Enum):
    """Prefix Enum that identifies the base character for each mode."""
    ALPHANUMERIC = "a"
    NUMERIC = "0"