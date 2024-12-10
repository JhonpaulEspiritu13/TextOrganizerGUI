"""
* Name         : Text Prefix Select GUI (text_prefix_select_gui.py)
* Author       : Jhon Paul Espiritu
* Created      : 12/10/2024
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

class TextPrefixSelectWindow(tk.Toplevel):
    """Top Level window that helps users select a prefix."""
    def __init__(self, prefix_list = []):
        """Initializes a tkinter gui with other elements."""
        # Initialize tk like normal.
        super().__init__()
        self.prefix_list = prefix_list
        self._initialize_tkinter_window()
        self._define_tkinter_properties()

    # ================ Private Functions

    def _initialize_tkinter_window(self):
        """Initialize all the elements for prefix selecting."""
        # Listbox that initializes all prefixes.
        self.prefix_listbox = tk.Listbox(self, width=20, height=12, selectmode="browse")
        self.prefix_listbox.grid(row=0)
        for prefix in self.prefix_list:
            self.prefix_listbox.insert("end", prefix)
        # Frame and buttons for selecting prefixes.
        self.prefix_button_frame = tk.LabelFrame(self, width=125, height=50, text="Select A Prefix")
        self.prefix_button_frame.grid_propagate(False)
        self.prefix_button_frame.grid(row=1)
        self.prefix_button_select_prefix = tk.Button(self.prefix_button_frame, width=7, text="Select", command=self._get_selected_prefix)
        self.prefix_button_select_prefix.grid(row=0, column=0)
        self.prefix_button_exit_prefix = tk.Button(self.prefix_button_frame, width=7, text="Exit", command=self.destroy)
        self.prefix_button_exit_prefix.grid(row=0, column=1)

    def _get_selected_prefix(self):
        """Get the selected prefix from the listbox."""
        self.selected_prefix = self.prefix_listbox.get(tk.ACTIVE)
        self.destroy()

    def _define_tkinter_properties(self):
        """Defines the tkinter element properties."""
        self.title("Select a Custom Prefix")
        self.resizable(False, False)
        # Stops main window from being interacted with until this window is destroyed.
        self.grab_set()
        self.transient(self.master)
        self.master.wait_window(self)