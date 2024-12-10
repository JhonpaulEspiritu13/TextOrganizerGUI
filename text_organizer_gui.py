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
import os
import tkinter as tk
import tkinter.ttk as tkk
from tkinter import filedialog
# Classes
from text_prefix_select_gui import TextPrefixSelectWindow
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
        self.directory_frame = tk.LabelFrame(self, height=425, text="File Explorer")
        self.directory_frame.grid(row=1, column=0)
        self.button_frame = tk.LabelFrame(self, width=130, height=460, text="Command List")
        self.button_frame.grid_propagate(False)
        self.button_frame.grid(row=1, column=1)

    def _initialize_directory_frame_elements(self):
        """Initializes the framework for the directory file explorer."""
        self.listbox_list = []
        # Directory listbox
        self.directory_listbox_label = tk.Label(self.directory_frame, text="Directory List")
        self.directory_listbox_label.grid(row=0, column=0)
        self.directory_listbox = tk.Listbox(self.directory_frame, width=20, height=12, selectmode="extended", exportselection=False)
        self.directory_listbox.grid(row=1, column=0)
        self.directory_listbox.bind("<<ListboxSelect>>", lambda event: self._change_selected_listbox_index(event, 0, "Directory"))
        self.listbox_list.append(self.directory_listbox)
        # Separator
        tkk.Separator(self.directory_frame, orient="horizontal").grid(row=2, sticky="ew", pady=3)
        # File Listbox
        self.file_listbox_label = tk.Label(self.directory_frame, text="File List")
        self.file_listbox_label.grid(row=3, column=0)
        self.file_listbox = tk.Listbox(self.directory_frame, width=20, height=12, selectmode="extended", exportselection=False)
        self.file_listbox.grid(row=4, column=0)
        self.file_listbox.bind("<<ListboxSelect>>", lambda event: self._change_selected_listbox_index(event, 1, "File"))
        self.listbox_list.append(self.file_listbox)

    def _initialize_button_frame_elements(self):
        """Initializes the framework for the button frames."""
        # Prefix frame
        self.button_prefix_frame = tk.LabelFrame(self.button_frame, width=125, height=190, text="Prefix Commands")
        self.button_prefix_frame.grid_propagate(False)
        self.button_prefix_frame.grid(row=0)
        self._initialize_prefix_frame_buttons()
        # Sort frame
        self.button_sort_frame = tk.LabelFrame(self.button_frame, width=125, height=120, text="Name Commands")
        self.button_sort_frame.grid_propagate(False)
        self.button_sort_frame.grid(row=1)
        self._initialize_sort_frame_buttons()
        # Custom Prefix Frame
        self.button_custom_frame = tk.LabelFrame(self.button_frame, width=125, height=130, text="Custom Prefix")
        self.button_custom_frame.grid_propagate(False)
        self.button_custom_frame.grid(row=2)
        self._initialize_custom_frame_buttons()

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
        # Buttons for incrementing prefix mode.
        self.button_prefix_frame_increment_frame = tk.LabelFrame(self.button_prefix_frame, width=125, height=50, text="Increment Prefixes")
        self.button_prefix_frame_increment_frame.grid(row=5)
        self.button_prefix_frame_plus_button = tk.Button(self.button_prefix_frame_increment_frame, text=f"+", width=7, command=self._increment_prefix_base)
        self.button_prefix_frame_plus_button.grid(row=0, column=0)
        self.button_prefix_frame_minus_button = tk.Button(self.button_prefix_frame_increment_frame, text=f"-", width=7, command=self._decrement_prefix_base)
        self.button_prefix_frame_minus_button.grid(row=0, column=1)


    def _initialize_sort_frame_buttons(self):
        """Initializes the button sort frame buttons."""
        # Label for deciding the currently selected list box.
        self.button_sort_frame_selected_listbox_label = tk.Label(self.button_sort_frame, justify=tk.LEFT, anchor="w", font="bold 10", text="Selected Listbox:")
        self.button_sort_frame_selected_listbox_label.grid(row=0)
        self.button_sort_frame_selected_listbox_textbox = tk.Text(self.button_sort_frame, width=10, height=1, state="disabled", bg="gray90")
        self.button_sort_frame_selected_listbox_textbox.grid(row=1)
        # Separator
        tkk.Separator(self.button_sort_frame, orient="horizontal").grid(row=2, sticky="ew", pady=3)
        # Prefixing buttons, for actually adding prefixes to a listbox.
        self.button_sort_frame_prefix_all_button = tk.Button(self.button_sort_frame, text="Prefix All", width=15, command=self._prefix_all)
        self.button_sort_frame_prefix_some_button = tk.Button(self.button_sort_frame, text="Prefix Selected", width=15, command=self._prefix_selected)
        self.button_sort_frame_prefix_all_button.grid(row=3)
        self.button_sort_frame_prefix_some_button.grid(row=4)

    def _initialize_custom_frame_buttons(self):
        """Initializes the button custom prefix frame buttons."""
        # Label and textbox
        self.button_custom_frame_custom_prefix_label = tk.Label(self.button_custom_frame, justify=tk.LEFT, anchor="w", font="bold 10", text=" Type Valid Prefix:")
        self.button_custom_frame_custom_prefix_label.grid(row=0)
        self.button_custom_frame_custom_prefix_textbox = tk.Text(self.button_custom_frame, width=10, height=1)
        self.button_custom_frame_custom_prefix_textbox.grid(row=1)
        # Buttons
        self.button_custom_frame_set_prefix_button = tk.Button(self.button_custom_frame, text="Set Custom Prefix", width=15, command=lambda: self._set_custom_prefix(self.button_custom_frame_custom_prefix_textbox.get("1.0","end-1c")))
        self.button_custom_frame_save_prefix_button = tk.Button(self.button_custom_frame, text="Save Current Prefix", width=15, command=lambda: self._save_custom_prefix(self.button_custom_frame_custom_prefix_textbox.get("1.0","end-1c")))
        self.button_custom_frame_set_prefix_button.grid(row=2)
        tkk.Separator(self.button_custom_frame, orient="horizontal").grid(row=3, sticky="ew", pady=3)
        self.button_custom_frame_save_prefix_button.grid(row=4)

    def _initialize_menu_bar_elements(self):
        """Initializes the elements for opening files/folders, closing files, etc."""
        # File Tab
        self.menu_bar_file = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar_file.add_command(label="Open Directory", command=self.open_directory_dialog)
        self.menu_bar_file.add_separator()
        self.menu_bar_file.add_command(label="Refresh Directory", command=self.refresh_directory_files)
        self.menu_bar_file.add_command(label="Save Directory", command=self.save_directory_files)
        self.menu_bar_file.add_separator()
        self.menu_bar_file.add_command(label="Close Program", command=self.destroy)
        self.menu_bar.add_cascade(label="Folder", menu=self.menu_bar_file)
        # Prefix Tab
        self.menu_bar_prefix = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar_prefix.add_command(label="Load Prefix", command=self._load_custom_prefix)
        self.menu_bar_prefix.add_command(label="Save Prefix", command=lambda: self._save_custom_prefix(self.button_custom_frame_custom_prefix_textbox.get("1.0","end-1c")))
        self.menu_bar.add_cascade(label="Prefixes", menu=self.menu_bar_prefix)

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
        # Changes associated label.
        self.button_prefix_frame_current_prefix_label_2.configure(text=f"Prefix: {self.selected_prefix_base}")

    @property
    def custom_prefix_actual(self):
        """The actual custom prefix used when PrefixMode is set to CUSTOM."""
        return self._custom_prefix_actual

    @custom_prefix_actual.setter
    def custom_prefix_actual(self, value):
        """The actual custom prefix used when PrefixMode is set to CUSTOM
        
        :param value: Folder/File accessible string.
        :raise ValueError: If the given value cannot be used in folders, raise ValueError."""
        # Value is empty.
        if not value:
            raise ValueError
        # Characters that cannot be used in folders.
        folder_characters = set('[\\/*?:"<>|]')
        # Iterates through each character in value, checking if they have the characters above.
        # Probably not the most efficient way? But will get the job done for this project.
        if any(char in value for char in folder_characters):
            raise ValueError    
        self._custom_prefix_actual = value
        # Refresh prefix if set to custom.
        if self.selected_prefix_mode == PrefixMode.CUSTOM:
            self._change_selected_prefix_mode(PrefixMode.CUSTOM)

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

        # Constants used for reading/writing
        self.PREFIX_FILE_NAME = "file_prefixes.txt"

    def _change_selected_listbox_index(self, event, index: int, name: str) -> None:
        """Bind function for listbox: Changes the value of the current
           selected list box index.
           
           :param index: int - index to change
           :param name: str - name to set listbox"""
        self.selected_list_box_index = index
        # Textbox Change
        self.button_sort_frame_selected_listbox_textbox.configure(state="normal")
        self.button_sort_frame_selected_listbox_textbox.delete(1.0, tk.END)
        self.button_sort_frame_selected_listbox_textbox.insert(tk.END, name)
        self.button_sort_frame_selected_listbox_textbox.configure(state="disable")
        

    def _change_selected_prefix_mode(self, value) -> None:
        """Command function for changing the current selected prefix.
        
        :param value: Prefix mode required."""
        self.selected_prefix_mode = value
    
    def _change_selected_prefix_base(self, mode) -> None:
        """Set the selected prefix base. Dependant on mode. If the mode is set to custom, change to the custom base.
        
        :param mode: The prefix mode that is currently set."""
        if mode == PrefixMode.CUSTOM:
            try:
                # Show the custom prefix set.
                self.selected_prefix_base = self.custom_prefix_actual
            except AttributeError:
                # Custom prefix has not been set yet.
                tk.messagebox.showerror("No Prefix Set", "No custom prefix was set.\n\n Defaulting to Alphanumeric.")
                # Default back to alphanumeric mode.
                self._change_selected_prefix_mode(PrefixMode.ALPHANUMERIC)
        else:
            # Otherwise choose the mode.
            self.selected_prefix_base = PrefixBase[self.selected_prefix_mode.name].value

    def _increment_prefix_base(self) -> None:
        """Increments the prefix base depending on mode.
           Alphanumeric: a-z
           Numeric: 0-9
           Custom: None"""
        old_prefix_base = self.selected_prefix_base
        # (a-z) Alphanumeric Increment
        if self.selected_prefix_mode == PrefixMode.ALPHANUMERIC:
            if old_prefix_base == "z":
                # Goes back to "a" if at the end
                self.selected_prefix_base = "a"
            else:
                # Converts to the ascii value, increments by one, then reconverts it back to char.
                self.selected_prefix_base = chr(ord(old_prefix_base) + 1)
        # (0-9) Numeric increment
        elif self.selected_prefix_mode == PrefixMode.NUMERIC:
            old_prefix_base = int(old_prefix_base) # Convert to integer for checking
            if old_prefix_base == 9:
                # Goes back to 0 if at the end
                self.selected_prefix_base = "0"
            else:
                # Back to string after incrementing
                self.selected_prefix_base = str(old_prefix_base + 1)
        # Nothing for customs or other modes. Would otherwise need to be added.

    def _decrement_prefix_base(self) -> None:
        """Decrements the prefix base depending on mode.
           Alphanumeric: a-z
           Numeric: 0-9
           Custom: None"""
        old_prefix_base = self.selected_prefix_base
        # (a-z) Alphanumeric Decrement
        if self.selected_prefix_mode == PrefixMode.ALPHANUMERIC:
            if old_prefix_base == "a":
                # Goes to "z" if at the start
                self.selected_prefix_base = "z"
            else:
                # Converts to the ascii value, decrements by one, then reconverts it back to char.
                self.selected_prefix_base = chr(ord(old_prefix_base) - 1)
        # (0-9) Numeric Decrement
        elif self.selected_prefix_mode == PrefixMode.NUMERIC:
            old_prefix_base = int(old_prefix_base) # Convert to integer for checking
            if old_prefix_base == 0:
                # Goes back to 0 if at the end
                self.selected_prefix_base = "9"
            else:
                # Back to string after incrementing
                self.selected_prefix_base = str(old_prefix_base - 1)
        # Nothing for customs or other modes. Would otherwise need to be added.

    def _prefix_all(self):
        """Add the current prefix to all elements."""
        selected_listbox = self.listbox_list[self.selected_list_box_index]
        selected_dictionary = self.get_selected_dict()
        # Loops through the selected items tuple.
        all_items = selected_listbox.get(0, tk.END)
        for actual_item in all_items:
            # Selected item, and selected item with prefix.
            new_item = self.selected_prefix_base + actual_item
            # Pops the current item with the newly created prefixed item.
            selected_dictionary[new_item] = selected_dictionary[actual_item]
            del selected_dictionary[actual_item]
        # Refreshes textbox because keys have been changed!
        self._sort_listboxes()
        self._refresh_listboxes()

    def _prefix_selected(self):
        """Add the current prefix to a select few elements."""
        selected_listbox = self.listbox_list[self.selected_list_box_index]
        selected_dictionary = self.get_selected_dict()
        # Loops through the selected items tuple.
        selected_items = selected_listbox.curselection()
        for item in selected_items:
            # Selected item, and selected item with prefix.
            actual_item = selected_listbox.get(item)
            new_item = self.selected_prefix_base + actual_item
            # Pops the current item with the newly created prefixed item.
            selected_dictionary[new_item] = selected_dictionary[actual_item]
            del selected_dictionary[actual_item]
        # Refreshes textbox because keys have been changed!
        self._sort_listboxes()
        self._refresh_listboxes()

    def _set_custom_prefix(self, value):
        """Sets the current custom prefix. Handles error with messagebox."""
        try:
            # Removes leading whitespaces, newlines and tab characters.
            self.custom_prefix_actual = value.replace("\n", "").lstrip()
        except ValueError:
            tk.messagebox.showerror("Invalid Prefix", "A folder/file cannot be prefixed with this.")

    def _load_custom_prefix(self):
        """Loads the prefixes folder and opens a window for user to select a prefix."""
        try:
            prefixes = []
            # Attempts to open file
            with open(self.PREFIX_FILE_NAME, 'r') as f:
                for line in f.readlines():
                    # Strips all newspaces and whitespaces from list.
                    append_line = line.replace("\n", "").replace("\r", "").replace("\t", "").lstrip()
                    # Reads each line in the file.
                    if append_line: # Ensure it's not empty.
                        prefixes.append(append_line)
            # Ensures prefix list is not empty.
            if not prefixes:
                raise PrefixListEmptyException
            prefix_select_window = TextPrefixSelectWindow(prefixes)
            # After window is done running, set the custom prefix!
            self._set_custom_prefix(prefix_select_window.selected_prefix)
        except FileNotFoundError:
            tk.messagebox.showerror("Prefix File Not Found", "Prefixes file not found. Ensure that you've created the file and that its placed in the correct directory.")
        except PrefixListEmptyException:
            tk.messagebox.showerror("Prefix File Empty", "The current prefix file list is empty. Please add new prefixes.")
        except AttributeError:
            pass

    def _save_custom_prefix(self, value):
        """Saves the current custom prefix to a file."""
        # Tries to set the current prefix
        try:
            # Removes leading whitespaces, newlines and tab characters.
            self.custom_prefix_actual = value.replace("\n", "").lstrip()
            # Appends to end of file, writes a new file if it does not exist.
            with open(self.PREFIX_FILE_NAME, 'a+') as f:
                f.write(self.custom_prefix_actual + "\n")
        except ValueError:
            tk.messagebox.showerror("Invalid Prefix", "A folder/file cannot be prefixed with this. Not saved to file.")

    def _sort_listboxes(self):
        """Sorts the dictionaries."""
        # Lambda function helps sorts by lower case key (Leaving them capital results in capital files having bigger priority.)
        self.dict_directories = dict(sorted(self.dict_directories.items(), key=lambda i: i[0].lower()))
        self.dict_files = dict(sorted(self.dict_files.items(), key=lambda i: i[0].lower()))

    def _refresh_listboxes(self):
        for listbox in self.listbox_list:
            listbox.delete(0,tk.END)
        """For each key in the listbox dictionaries, add it to the end of each listbox."""
        for directory in self.dict_directories.keys():
            self.directory_listbox.insert("end", directory)
        for file in self.dict_files.keys():
            self.file_listbox.insert("end", file)

    # ================ Normal Functions

    def get_selected_dict(self):
        """Messy way of handling dictionary returns, but it seems
           that storing dictionary references in a list does not work.
           This will have to do for now."""
        if self.selected_list_box_index == 0:
            return self.dict_directories
        elif self.selected_list_box_index == 1:
            return self.dict_files
        else:
            return None

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
            self.dict_directories = {}
            self.dict_files = {}
            self.file_directory.read_file_list()
            # For each value in the file dictionary, append it to the file directory.
            for directory in self.file_directory.get_directory_values():
                self.dict_directories[directory] = directory
            for file in self.file_directory.get_file_values():
                self.dict_files[file] = file
            self._refresh_listboxes()
        except InvalidDirectoryPath:
            tk.messagebox.showerror("Invalid Directory Path", "The previous directory could not be opened. Check if it has been renamed or removed.")

    def refresh_directory_files(self):
        """Refreshes a selected directory."""
        try:
            self.open_directory_files()
        except AttributeError:
            # There is no directory to refresh.
            tk.messagebox.showerror("No Directory Selected", "No directory has been selected to be refreshed.")

    def save_directory_files(self):
        """Saves any newly created items in listbox. Note: This handles the saving to file
           paths since I thought it'd be better to reinitialize the file directory."""
        try:
            path = self.file_directory.directory_path
            # Directory renaming
            for key, value in self.dict_directories.items():
                original_path = os.path.join(path, value)
                new_path = os.path.join(path, key)
                os.rename(original_path, new_path)

            # File renaming
            for key, value in self.dict_files.items():
                original_path = os.path.join(path, value)
                new_path = os.path.join(path, key)
                os.rename(original_path, new_path)

            # Refreshes after every file and directory is saved
            self.open_directory_files()
        except AttributeError:
            tk.messagebox.showerror("No Directory Selected", "No directory has been selected to be saved to.")
        except FileNotFoundError:
            tk.messagebox.showerror("File not found.", "A file seems to have been deleted or renamed. Some files may have potentially been renamed, but processes have stopped.\n\nContents have not been refreshed.")
        
if __name__ == '__main__':
    new_gui = TextOrganizerGUI()
    new_gui.mainloop()