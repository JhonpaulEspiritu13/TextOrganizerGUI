"""
* Name         : Text Organizer GUI (text_organizer_gui.py)
* Author       : Jhon Paul Espiritu
* Created      : 11/26/2024
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : This is a Text Organizer GUI for the python final project.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

# Imports
import tkinter as tk
from tkinter import filedialog
# Classes
from classes.exceptions import *
from classes.file_directory import FileDirectory

class TextOrganizerGUI(tk.Tk):
    """GUI Class that inherits from tkinter."""
    def __init__(self):
        """Initializes a tkinter gui with other elements."""
        # Initialize tk like normal.
        super().__init__()
        # Initializes the LabelFrames for holding other GUI elements.
        self._initialize_core_elements()
        # Initializes the directory explorer.
        self._initialize_directory_frame_elements()
        # Initializes the menu bar.
        self._initialize_menu_bar_elements()
        # Initializes the properties.
        self.define_properties()
    
    def _initialize_core_elements(self):
        """Initializes the core framework visual
        elements that are held within the GUI."""
        # Menu bar initialization
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        # Label Frames
        self.directory_frame = tk.LabelFrame(self, width=200, height=300, text="Directory Explorer")
        self.directory_frame.grid(row=1, column=0)
        self.button_frame = tk.LabelFrame(self, width=100, height=300, text="Command List")
        self.button_frame.grid(row=1, column=1)

    def _initialize_directory_frame_elements(self):
        """Initializes the framework for the directory file explorer."""
        self.directory_listbox = tk.Listbox(self.directory_frame, width=15, height=18)
        self.directory_listbox.grid(row=0, column=0)

    def _initialize_menu_bar_elements(self):
        """Initializes the elements for opening files/folders, closing files, etc."""
        # File Tab
        self.menu_bar_file = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar_file.add_command(label="Open Directory", command=self.open_directory_dialog)
        self.menu_bar.add_cascade(label="File", menu=self.menu_bar_file)

    def open_directory_dialog(self):
        """Opens a directory dialog to check a specified user directory."""
        try:
            directory = filedialog.askdirectory(title="Open Directory")
            self.file_directory = FileDirectory(directory)
        # File directory could not be found.
        except InvalidDirectoryPath:
            tk.messagebox.showerror("Invalid Directory Path", "This directory could not be opened.")
        # File directory was not a string (should not happen).
        except InvalidDirectoryFormat:
            tk.messagebox.showerror("Invalid Directory Format", "This directory is not the correct format. Contact developer with this error.")
        # Folder Dialog was cancelled, pass.
        except NoDirectoryPath:
            pass

    def define_properties(self):
        """Defines the tkinter properties."""
        self.title("Text Organizer")
        self.resizable(False, False)
        
if __name__ == '__main__':
    new_gui = TextOrganizerGUI()
    new_gui.mainloop()