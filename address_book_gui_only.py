"""
    Name: address_book_gui_only.py
    Author: Jed Felker
    Created: 02/14/23
    Tkinter version of address book
"""

# Import tkinter library
from tkinter import *
# Override tk widgets with nicer looking ttk themed widgets
from tkinter.ttk import *


class AddressBook:
    def __init__(self):
        # Initialize the Tkinter GUI
        self.init_gui()
        # Start the main Tkinter program loop
        mainloop()

# ------------------ INITIALIZE GUI ------------------------------------#
    def init_gui(self):
        """Initalize program GUI"""
        self.window = Tk()
        # Set window location on screen 400 pixels right 300 pixels down
        # The window size will change based on the controls
        self.window.geometry("+400+300")
        # Add icon to program title bar
        self.window.iconbitmap("address_book.ico")
        self.window.title("Address Book")
        self.window.resizable(False, False)
        # Create and grid all widgets
        self.create_frames()
        self.create_widgets()
        self.create_treeview()

# --------------------------- CREATE FRAMES ----------------------------#
    def create_frames(self):
        self.entry_frame = LabelFrame(
            self.window,
            text="Enter Contact Info",
            relief=GROOVE
        )
        self.operations_frame = LabelFrame(
            self.window,
            text="Record Operations",
            relief=GROOVE
        )
        self.treeview_frame = LabelFrame(
            self.window,
            text="Contact List",
            relief=GROOVE
        )
        # Grid the frames
        self.entry_frame.grid(row=0, column=0, sticky=NW)
        self.operations_frame.grid(row=0, column=1, sticky=N)
        self.treeview_frame.grid(row=1, column=0, columnspan=2, sticky=W)

# ------------------------- CREATE WIDGETS -----------------------------#
    def create_widgets(self):
        # ------------------------ CREATE LABELS -----------------------#
        self.lbl_first_name = Label(
            self.entry_frame, text="First Name:", anchor="e")
        self.lbl_last_name = Label(
            self.entry_frame, text="Last Name:", anchor="e")
        self.lbl_phone = Label(self.entry_frame, text="Phone:", anchor="e")
        self.lbl_email = Label(
            self.entry_frame, text="Email:", anchor="e")
        self.lbl_status = Label(self.entry_frame, text=" ", anchor="e")

        # --------------------- CREATE ENTRY BOXES ---------------------#
        self.first_name_entry = Entry(self.entry_frame, width=30)
        # Set focus for data entry
        self.first_name_entry.focus_set()
        self.last_name_entry = Entry(self.entry_frame, width=30)
        self.phone_entry = Entry(self.entry_frame, width=30)
        self.email_entry = Entry(self.entry_frame, width=30)

        # -------------------- CREATE BUTTON ---------------------------#
        self.btn_add = Button(
            self.operations_frame,
            text="Add"
        )
        self.btn_modify = Button(
            self.operations_frame,
            text="Update Selected"
        )
        self.btn_delete = Button(
            self.operations_frame,
            text="Delete Selected"
        )

        # --------------------- GRID WIDGETS ---------------------------#
        self.lbl_first_name.grid(row=0, column=0)
        self.lbl_last_name.grid(row=1, column=0)
        self.lbl_phone.grid(row=2, column=0)
        self.lbl_email.grid(row=3, column=0)
        self.lbl_status.grid(row=4, column=0, columnspan=2)

        self.first_name_entry.grid(row=0, column=1)
        self.last_name_entry.grid(row=1, column=1)
        self.phone_entry.grid(row=2, column=1)
        self.email_entry.grid(row=3, column=1)

        self.btn_add.grid(row=0, column=0, sticky=EW)
        self.btn_modify.grid(row=1, column=0, sticky=EW)
        self.btn_delete.grid(row=2, column=0, sticky=EW)

        # Set padding between frame and window
        self.entry_frame.grid_configure(padx=20, pady=(20))
        self.operations_frame.grid_configure(padx=20, pady=(20))
        # Even out the padding between frames, leave out y distance on top
        self.treeview_frame.grid_configure(padx=20, pady=(0, 20))

        # Set padding for all widgets inside the frame
        for widget in self.entry_frame.winfo_children():
            widget.grid_configure(padx=7, pady=7)
        for widget in self.treeview_frame.winfo_children():
            widget.grid_configure(padx=7, pady=7)
        for widget in self.operations_frame.winfo_children():
            widget.grid_configure(padx=7, pady=7)

# ------------------------ TREEVIEW AND SCROLLBAR ---------------------#
    def create_treeview(self):
        """Setup tree view for record display"""
        # Create treeview
        self.tree = Treeview(
            self.treeview_frame,
            height=10,
            columns=("id", "first_name", "last_name", "phone", "email"),
            style="Treeview",
            show="headings",
            selectmode="browse"
        )
        # Setup the columns
        self.tree.column("id", width=30)
        self.tree.column("first_name", width=120)
        self.tree.column("last_name", width=120)
        self.tree.column("phone", width=120)
        self.tree.column("email", width=175)

        # Setup the heading text visible at the top of the column
        self.tree.heading("id", text="ID", anchor=W)
        self.tree.heading("first_name", text="First Name", anchor=W)
        self.tree.heading("last_name", text="Last Name", anchor=W)
        self.tree.heading("phone", text="Phone", anchor=W)
        self.tree.heading("email", text="Email", anchor=W)

        # Grid the tree
        self.tree.grid(row=0, column=0)

        # Create scrollbar for treeview
        self.scrollbar = Scrollbar(
            self.treeview_frame,
            orient="vertical",
            command=self.tree.yview
        )

        # Set scroll bar to scroll vertically and attach to the tree
        self.tree.configure(yscroll=self.scrollbar.set)

        # Grid scrollbar just to the right of the tree
        # sn (SouthNorth) expands scrollbar to height of tree
        self.scrollbar.grid(row=0, column=1, sticky="sn")


# -------------------- START PROGRAM ----------------------#
address_book = AddressBook()