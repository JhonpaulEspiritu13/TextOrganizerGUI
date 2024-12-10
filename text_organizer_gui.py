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
import tkinter.ttk as tkk
from tkinter import filedialog
# Classes
from classes.exceptions import *
from classes.enums import *
from classes.file_directory import FileDirectory

class TextOrganizerGUI(tk.Tk):
    """GUI Class that inherits from tkinter."""
    def __init__(self):
        """Initializes a tkinter gui with other elements."""
        # Initialize tk like normal.
        super().__init__()
        # Initializes the properties.
        self._define_tkinter_properties()

        # Initializes the LabelFrames for holding other GUI elements (Core elements)
        self._initialize_core_elements()
        # Initializes the elements inside the core label frames.
        self._initialize_directory_frame_elements()
        self._initialize_button_frame_elements()
        # Initializes the menu bar.
        self._initialize_menu_bar_elements()
        # Initializes the properties.
        self._define_class_properties()
    
    # ================ Initialize Elements

    def _initialize_core_elements(self):
        """Initializes the core framework visual
        elements that are held within the GUI."""
        # Menu bar initialization
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        # Label Frames
        self.directory_frame = tk.LabelFrame(self, width=200, height=320, text="File Explorer")
        self.directory_frame.grid(row=1, column=0)
        self.button_frame = tk.LabelFrame(self, width=130, height=355, text="Command List")
        self.button_frame.grid_propagate(False)
        self.button_frame.grid(row=1, column=1)

    def _initialize_directory_frame_elements(self):
        """Initializes the framework for the directory file explorer."""
        self.listbox_list = []
        # Directory listbox
        self.directory_listbox_label = tk.Label(self.directory_frame, text="Directory List")
        self.directory_listbox_label.grid(row=0, column=0)
        self.directory_listbox = tk.Listbox(self.directory_frame, width=15, height=9)
        self.directory_listbox.grid(row=1, column=0)
        #self.directory_listbox.bind("<<ListboxSelect>>", lambda event: self._change_selected_listbox(event, 0))
        self.listbox_list.append(self.directory_listbox)
        # Separator
        tkk.Separator(self.directory_frame, orient="horizontal").grid(row=2, sticky="ew", pady=3)
        # File Listbox
        self.file_listbox_label = tk.Label(self.directory_frame, text="File List")
        self.file_listbox_label.grid(row=3, column=0)
        self.file_listbox = tk.Listbox(self.directory_frame, width=15, height=9)
        self.file_listbox.grid(row=4, column=0)
        #self.file_listbox.bind("<<ListboxSelect>>", lambda event: self._change_selected_listbox(event, 1))
        self.listbox_list.append(self.file_listbox)

    def _initialize_button_frame_elements(self):
        """Initializes the framework for the button frames."""
        # Prefix frame
        self.button_prefix_frame = tk.LabelFrame(self.button_frame, width=125, height=150, text="Prefix Commands")
        self.button_prefix_frame.grid_propagate(False)
        self.button_prefix_frame.grid(row=0)
        self._initialize_prefix_frame_buttons()
        # Sort frame
        self.button_sort_frame = tk.LabelFrame(self.button_frame, width=125, height=100, text="Name Commands")
        self.button_sort_frame.grid_propagate(False)
        self.button_sort_frame.grid(row=1)
        self._initialize_sort_frame_buttons()

    def _initialize_prefix_frame_buttons(self):
        """Initializes the button prefix frame buttons."""
        # Labels
        self.button_prefix_frame_current_prefix_label_1 = tk.Label(self.button_prefix_frame, justify=tk.LEFT, anchor="w", font="bold 10", text=f"Mode: {PrefixName.ALPHANUMERIC.value}")
        self.button_prefix_frame_current_prefix_label_1.grid(row=0)
        self.button_prefix_frame_current_prefix_label_2 = tk.Label(self.button_prefix_frame, justify=tk.LEFT, anchor="w", font="bold 10", text=f"Prefix: {PrefixBase.ALPHANUMERIC.value}")
        self.button_prefix_frame_current_prefix_label_2.grid(row=1)
        # Buttons for setting the prefix mode.
        self.button_prefix_frame_alpha_button = tk.Button(self.button_prefix_frame, text=f"Set Mode: {PrefixName.ALPHANUMERIC.value}", width=15, command=lambda: self._change_selected_prefix_mode(PrefixMode.ALPHANUMERIC))
        self.button_prefix_frame_alpha_button.grid(row=2)
        self.button_prefix_frame_numer_button = tk.Button(self.button_prefix_frame, text=f"Set Mode: {PrefixName.NUMERIC.value}", width=15, command=lambda: self._change_selected_prefix_mode(PrefixMode.NUMERIC))
        self.button_prefix_frame_numer_button.grid(row=3)
        self.button_prefix_frame_custom_button = tk.Button(self.button_prefix_frame, text=f"Set Mode: {PrefixName.CUSTOM.value}", width=15, command=lambda: self._change_selected_prefix_mode(PrefixMode.CUSTOM))
        self.button_prefix_frame_custom_button.grid(row=4)


    def _initialize_sort_frame_buttons(self):
        """Initializes the button sort frame buttons."""
        self.button_sort_frame_up_button = tk.Button(self.button_sort_frame, text="Sort Up", width=15, command=self.sort_up)
        self.button_sort_frame_down_button = tk.Button(self.button_sort_frame, text="Sort Down", width=15)
        self.button_sort_frame_up_button.grid(row=0)
        self.button_sort_frame_down_button.grid(row=1)

    def _initialize_menu_bar_elements(self):
        """Initializes the elements for opening files/folders, closing files, etc."""
        # File Tab
        self.menu_bar_file = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar_file.add_command(label="Open Directory", command=self.open_directory_dialog)
        self.menu_bar.add_cascade(label="File", menu=self.menu_bar_file)

    # ================ Properties

    @property
    def selected_list_box_index(self):
        """Selected listbox index needed when sorting files."""
        return self._selected_list_box_index
    
    @selected_list_box_index.setter
    def selected_list_box_index(self, value):
        """Defines the selected listbox index. Cannot be more than max number of listboxes.
        
        :param value: int - Index to set.
        :raise ValueError: Not a valid index id.
        :raise OverSelectedListboxIndex: Over the amount of listboxes to select"""
        if (value < 0):
            raise ValueError
        if (value >= len(self.listbox_list)):
            raise OverSelectedListboxIndex
        self._selected_list_box_index = value

    @property
    def selected_prefix_mode(self):
        """Selected prefix mode, used for identifying names and enums."""
        return self._selected_prefix_mode
    
    @selected_prefix_mode.setter
    def selected_prefix_mode(self, value):
        """Set the selected prefix mode. Needs to be in the enumerations list to be valid.
        
        :param value: The prefix mode to set to.
        :raise ValueError: Not a valid PrefixMode."""
        if value not in PrefixMode:
            raise ValueError
        # Sets both prefix mode and base.
        self._selected_prefix_mode = value
        self._change_selected_prefix_base(self._selected_prefix_mode)
        # Changes associated prefixes on labels.
        self.button_prefix_frame_current_prefix_label_1.configure(text=f"Mode: {PrefixName[self.selected_prefix_mode.name].value}")
        self.button_prefix_frame_current_prefix_label_2.configure(text=f"Prefix: {self.selected_prefix_base}")

    @property
    def selected_prefix_base(self):
        """Selected prefix base, used for adding prefixes to the start of files."""
        return self._selected_prefix_base
    
    @selected_prefix_base.setter
    def selected_prefix_base(self, value):
        """Sets the prefix base.
        
        :param value: str
        :raise ValueError: If the given value is not a string, raise an error."""
        if not isinstance(value, str):
            raise ValueError
        self._selected_prefix_base = value

    # ================ Private Functions

    def _define_tkinter_properties(self):
        """Defines the tkinter element properties."""
        self.title("Text Organizer")
        self.resizable(False, False)

    def _define_class_properties(self):
        """Defines the GUI element properties."""
        # Properties needed for working around the elements.
        self.selected_list_box_index = 0
        
        # Properties for prefixes.
        self.selected_prefix_mode = PrefixMode.ALPHANUMERIC

        # Dictionary that holds the file values.
        self.dict_directories = {}
        self.dict_files = {}

    def _change_selected_listbox(self, event, value: int) -> None:
        """Bind function for listbox: Changes the value of the current
           selected list box index.
           
           :param value: int - index to change"""
        self.selected_list_box_index = value

    def _change_selected_prefix_mode(self, value) -> None:
        """Command function for changing the current selected prefix.
        
        :param value: Prefix mode required."""
        self.selected_prefix_mode = value
    
    def _change_selected_prefix_base(self, mode) -> None:
        """Set the selected prefix base. Dependant on mode. If the mode is set to custom, change to the custom base.
        
        :param mode: The prefix mode that is currently set."""
        if mode == PrefixMode.CUSTOM:
            # Show the custom prefix set.
            self.selected_prefix_base = "Custom"
        else:
            # Otherwise choose the mode.
            self.selected_prefix_base = PrefixBase[self.selected_prefix_mode.name].value

    def sort_up(self):
        """Checks if an element is selected, and sorts that element up."""
        selected_listbox = self.listbox_list[self.selected_list_box_index]
        print(self.selected_list_box_index)
        print(selected_listbox.curselection())

    def _refresh_listboxes(self):
        """For each key in the listbox dictionaries, add it to the end of each listbox."""
        for directory in self.dict_directories.keys():
            self.directory_listbox.insert("end", directory)
        for file in self.dict_files.keys():
            self.file_listbox.insert("end", file)

    # ================ Normal Functions

    def open_directory_dialog(self):
        """Opens a directory dialog to check a specified user directory."""
        try:
            directory = filedialog.askdirectory(title="Open Directory")
            self.file_directory = FileDirectory(directory)
            self.open_directory_files()
        # File directory could not be found.
        except InvalidDirectoryPath:
            tk.messagebox.showerror("Invalid Directory Path", "This directory could not be opened.")
        # File directory was not a string (should not happen).
        except InvalidDirectoryFormat:
            tk.messagebox.showerror("Invalid Directory Format", "This directory is not the correct format. Contact developer with this error.")
        # Folder Dialog was cancelled, pass.
        except NoDirectoryPath:
            pass

    def open_directory_files(self):
        """Opens the directory and initializes them into a directory path list."""
        try:
            self.file_directory.read_file_list()
            # For each value in the file dictionary, append it to the file directory.
            for directory in self.file_directory.get_directory_values():
                self.dict_directories[directory] = directory
            for file in self.file_directory.get_file_values() :
                self.dict_files[file] = file
            self._refresh_listboxes()
        except InvalidDirectoryPath:
            tk.messagebox.showerror("Invalid Directory Path", "The previous directory could not be opened. Check if it has been renamed or removed.")
        
if __name__ == '__main__':
    new_gui = TextOrganizerGUI()
    new_gui.mainloop()