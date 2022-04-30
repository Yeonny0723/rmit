# room_type_gui.py

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox
from tkinter.messagebox import askyesno

from room_type_dao import RoomTypeDAO # To communicate with roomtype table
from validation import Validation


# #################
# RoomTypeGUI Class
# #################

class RoomTypeGUI():
    """RoomTypeGUI class to implement CRUD functionalities & methods to manage the user interface"""

    def __init__(self):   
        """Initialiser"""
        # Instantiate a data access object 
        # Contains methods to access the database
        self.room_type_dao = RoomTypeDAO()

        # Instantiate a validation object
        # Contains methods to validate input fields
        self.validator = Validation()

        # Form fields
        # Instantiate stringvars - hold  data entered in  fields of form
        self.room_type_id = tk.StringVar()
        self.room_type_tlt = tk.StringVar()
        self.king_bed_count = tk.IntVar()
        self.queen_bed_count = tk.IntVar()
        self.single_bed_count = tk.IntVar()
        self.bath_room_count = tk.IntVar()

        # List of room type ids - lb for listbox
        self.lb_ids = None

        # search
        self.search_room_type = None
        # search list
        self.ln_ids = None

        # Messagebox title
        self.mb_title_bar = "Room type CRUD"

    def create_gui(self, root):
        """
        Create a high level frame which contains the entire GUI 
        (of this part of the application) and adds it to the root window.
        Notice that the "root" window is passed the second parameter in the 
        method header.
        Also notice that the first (and mandatory) parameter to all methods 
        is "self" i.e. a reference to the object instantiated from the class.
        """

        # Good practice to print something at the start of the method 
        # e.g. which method is being executed, the values of parameters passes, 
        # etc
        # Good for tracing the execution of the program while debugging it
        # After debugging, you may want to "comment out" some of the 
        # print statements so that they do not execute and print too 
        # much stuff in the console
        print("\nCreating room type GUI ...")

        # room_type_frame = tk.Frame(root).pack() 
        # cannot write the above as pack() does not return anything
        # and need the variable name to refer to it elsewhere
        # DO NOT SPECIFY ANY WIDTH AND HEIGHT OF THE FRAMES 
        # HERE FOR FLEXIBILITY REASONS
        # The height and width or the root window can be specified 
        # in the main GUI (or in the main() method)
        room_type_frame = tk.Frame(root)
        room_type_frame.pack()

        # Add a frame to contain the form widgets
        # To put a number of widgets in a column one on top of the other, 
        # just use pack() without any options
        # Use the fill=tk.X option to make all widgets as wide as the parent widget
        # To pack widgets side by side, use the side option 
        # e.g. side=tk.LEFT, tk.BOTTOM, tk.RIGHT (default is tk.TOP)
        # Use the fill=tk.Y option to make all widgets as tall as the parent widget
        # have also fill=tk.BOTH option
        # The anchor= option is used to position the widget in the container, 
        # default is tk.CENTER
        # Internal padding around widgets: ipadx= and ipady=  default is 0
        # External padding arounf widgets: padx= pady=  default is 0
        form_frame = tk.Frame(room_type_frame)
        form_frame.pack()
    
        # row 0:  title label
        # The variable name is not needed
        # By default, the text is centered
        # To right align use anchor=e (east) not justify=RIGHT which is used 
        # for aligning multiple lines
        # Labels have padx= and pady= options but no ipadx= and ipady=
        # Check the ulr above, to finc out more about the many options 
        # available for configuring labels!!!
        # STICK TO THE DEFAULT VALUES,  
        # UNLESS YOU HAVE A GOOD REASON TO CHANGE THEM!!!!!!!!!!!!!!!!
        # For spanning multiple rows and columns, 
        # use rowspan= and columnspan= options (default is 1)
        # Use the sticky= option for positioning 
        # (instead of anchor= as used in pack) - 
        # (default is centered) values are: n, w, e, w, nw, etc
        # Internal padding around widgets: ipadx= and ipady=  default is 0
        # External padding around widgets: padx= pady=  default is 0
        # Use the width= option to specify how wide in terms of number of characters
        tk.Label(
            form_frame, 
            font=('arial', 10), 
            text = "Room type details").grid(row=0, column=0, columnspan=3)

        # row 1. room_type_id label, room_type_id entry and list_of_ids label
        tk.Label(
            form_frame, 
            text= "Room Type Id", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=1, column=0)
    
        tk.Entry(
            form_frame, 
            textvariable=self.room_type_id, 
            width=30, 
            bd=1, 
            state=tk.DISABLED).grid(row=1, column=1)
        # room_type_id is disabled to prevent user from entering a value
        # room_type_id is generated by the database because AUTOINCREMENT 
        # was specified in the database schema
        tk.Label(
            form_frame, 
            text= "Room type IDs", 
            font=('arial', 10)).grid(row=1, column=2)
        
        # ***search by search_room_type
        tk.Label(
            form_frame, 
            text= "Search by Room type", 
            font=('arial', 10)).grid(row=7, column=2)
        self.search_room_type = tk.Entry(form_frame)
        self.search_room_type.grid(row=8, column=2)

        # row 2. room_type label, room_type entry and listbox of ids
        tk.Label(
            form_frame, 
            text= "Room Type", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=2, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.room_type_tlt, 
            width=30, 
            bd=1).grid(row=2, column=1)

        
        # Use the height= option to specify the height, default is 10
        # Use the width= option to specify the number of characters, default is 20
        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=2, column=2, rowspan=5) 
        # 'self' means instance attribute rather than local variable
        # since python allows using variables before they are declared
        # it does not matter whether lb_ids has been declared or not at the 
        # top of the file before the methods definition
        # Set the method to be called when an item is clicked on the listbox 
        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)

        # row 3: king_bed_count label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "King bed counts", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=3, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.king_bed_count, 
            width=30, 
            bd=1).grid(row=3, column=1)

        # row 4: queen_bed_count label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Queen bed counts", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=4, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.queen_bed_count, 
            width=30, 
            bd=1).grid(row=4, column=1)

        # row 5: single_bed_count label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Single bed counts", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=5, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.single_bed_count, 
            width=30, 
            bd=1).grid(row=5, column=1)

        # row 6: bath_room_count label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Bathroom count", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=6, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.bath_room_count, 
            width=30, 
            bd=1).grid(row=6, column=1)

        # Buttons
        # There are 3 columns of widgets in the frame and 4 buttons
        # Better insert the button in another frame
        # Also easier to pack them from the left than using a grid with row 
        # and col locations
        # pady to leave a space from frame on top
        button_frame = tk.LabelFrame(room_type_frame, pady=10, text="Commands") 
        button_frame.pack()
        # Use the anchor= option to position the button
        # External padding around buttons: padx= pady=  default is 0
        # Use the width= option to specify the number of characters, 
        # otherwise calculated based on text width
        tk.Button(
            button_frame, 
            width=10, text="Clear", 
            command=self.clear_fields).pack(side=tk.LEFT)
        tk.Button(
            button_frame, 
            width=10, 
            text="Save", 
            command=self.save).pack(side=tk.LEFT)
        tk.Button(
            button_frame, 
            width=10, 
            text="Delete", 
            command=self.confirm_delete).pack(side=tk.LEFT)
        tk.Button(
            button_frame, 
            width=10, 
            text="Load", 
            command=self.load).pack(side=tk.LEFT)       
        tk.Button(
            button_frame, 
            width=10, 
            text="Search", 
            command=self.filter_by_room_type).pack(side=tk.LEFT)   
        # Return a reference to the high level frame created
        # Will need the reference to be able to destroy it in the calling function
        return room_type_frame

    def clear_fields(self):
        """Clear the fields of the form"""

        print("\nClearing fields ...")

        # Just blank all the fields
        self.room_type_id.set("")
        self.room_type_tlt.set("")
        self.king_bed_count.set("")
        self.queen_bed_count.set("")
        self.single_bed_count.set("")
        self.bath_room_count.set("")
        self.load()

    def save(self):
        """Save the data displayed on the form to the database."""


        print("\nSaving a room type ...")

        # Get the data
        data = self.get_fields()   

        # Validate the data
        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (len(data['room_type_id'])==0):
                # If nothing has been entered in room_type_id 
                # i.e. its length is zero characters
                print("Calling create() as room_type_id is absent")
                self.create(data)
            else:
                print("Calling update() as room_type_id is present")
                self.update(data)
                pass
        else:
            message_text = "Invalid fields.\n" + message 
            messagebox.showwarning(self.mb_title_bar, message_text, icon="warning")
            pass

        self.load()

    def confirm_delete(self):
        """
        Show confirmation popup before executing delete. 

        Parameters: None

        Return: None
        """
        answer = askyesno(title='confirmation',
                        message=f'Are you sure that you want to delete?')
        if answer:
            self.delete()
    
    def get_fields(self):
        """Get the data entered in the fields of the form"""

        print("\nGetting fields ...")

        room_type = {}
        # room_type_id is ignored when creating a record
        room_type['room_type_id'] = self.room_type_id.get() 
        room_type['room_type_tlt'] = self.room_type_tlt.get()
        room_type['king_bed_count'] = self.king_bed_count.get()
        room_type['queen_bed_count'] = self.queen_bed_count.get()
        room_type['single_bed_count'] = self.single_bed_count.get()
        room_type['bath_room_count'] = self.bath_room_count.get()

        print(f"room_type: {room_type}")
 
        return room_type    

    def create(self, data):
        """Create a new record in the database"""

        print("\nCreating a room_type ...")
        print(f"data: {data}")

        result = self.room_type_dao.create(data)

        # Display the returned message to the user - use a messagebox
        # Format: message.function(title, message [, options])
        # Functions: showinfo, showwarning, showerror, askquestion, 
        #            askokcancel, askyesno, or askretrycancel
        # Use the icon= option to specify which icon to display 
        # e.g. icon="warning", "error", "info", "question"     
        # Display everything that is returned in the result
        messagebox.showinfo(self.mb_title_bar, result)
        self.load()

    def update(self, data):
        """Update a record in the database"""

        print("\nUpdating a room type ...")
        print(f"data: {data}")

        result = self.room_type_dao.update(data['room_type_id'], data)

        # Display the returned message to the user - use a messagebox  
        # Display everything that is returned in the result      
        messagebox.showinfo(self.mb_title_bar, result)
        self.load()

    def delete(self):
        """Delete a record from the database"""

        print("\nDeleting  a room_type ...")
        
        # Grab the room_type_id from the stringvar
        id = self.room_type_id.get() 
        print(f"id: {id}")
        
        # Call the data access object to do the job
        # Pass the id as parameter to the delete() method
        result = self.room_type_dao.delete(id)   

        # Display the returned message to the user - use a messagebox    
        # Display everything that is returned in the result    
        messagebox.showinfo(self.mb_title_bar, result)
        self.load()

    def load(self):
        """Retrieve a list of IDs from the database and load them into a listbox"""

        print("\nLoading IDs in list box ...")

        result = self.room_type_dao.find_ids()
        print(f"result: {result}")

        # Check if there is an entry in the result dictionary
        if "room_type_ids" in result: 
            list_ids = result['room_type_ids'] # will crash if there is no entry!
            # Set the returned list into the listbox
            # Before doing that, must clear any previous list in the box
            self.lb_ids.delete(0,tk.END)
            print("Setting room_type_ids in listbox ...")
            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
                #print(x)
            pass

    def filter_by_room_type(self):
        """Retrieve a list of filtered IDs from the database and load them into a listbox"""

        print("\nLoading filtered IDs in list box ...")

        room_type_tlt = self.search_room_type.get()
        result = self.room_type_dao.find_by_room_type(room_type_tlt)

        if "filtered_room_types_ids" in result: 
            list_ids = result['filtered_room_types_ids'] # will crash if there is no entry!
            # Set the returned list into the listbox
            # Before doing that, must clear any previous list in the box
            self.lb_ids.delete(0,tk.END)
            print("Setting filtered_room_types_ids in listbox ...")
            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
                #print(x)
            pass

    def on_list_select(self, evt):
        """on_list_select() is triggered when a user clicks an item in the listbox"""

        print("\nSelecting an item from the list box ...")

        w = evt.widget

        # index = position of the item clicked in the list, first item is item 0 not 1
        index = int(w.curselection()[0]) 
          
         # value of the item clicked, in our case it's the room_type_id  
        value = w.get(index) 
         
        print(f"index: {index}") 
        print(f"value: {value}")

        # Call find_by_id and populate the stringvars of the form
        result = self.room_type_dao.find_by_id(value)

        # { "room_type" : {"room_type_id": "", "first_name": "", etc}}
        print(f"result: {result}") 

        # Grab room_type dict from result dict and use it to populate the fields on the form  
        room_type = result['room_type']
        self.populate_fields(room_type)

    def populate_fields(self, room_type):
        """Populate the fields of the form with data"""

        print("\nPopulating fields ...")
        print(f"room_type: {room_type}")

        # Set the values from the dict to the stringvars
        self.room_type_id.set(room_type['room_type_id'])
        self.room_type_tlt.set(room_type['room_type_tlt'])
        self.king_bed_count.set(room_type['king_bed_count'])
        self.queen_bed_count.set(room_type['queen_bed_count'])
        self.single_bed_count.set(room_type['single_bed_count'])
        self.bath_room_count.set(room_type['bath_room_count'])

    def validate_fields(self, data):
        """Validate the data entered in the fields of the form"""

        print("\nValidating the data ...")
        print(f"data: {data}")
           
        # By default set to true, anything wrong will turn it to false   
        valid_data = True 
        # Instantiate an empty list to contain the messages
        message_list = [] 
        
        # Check for blank fields
        # Do not check room_type_id as this is generated by the database

        if not str(data['room_type_tlt']):
            valid_data = False
            message_list.append("room type title is empty")
        if not str(data['king_bed_count']):
            valid_data = False
            message_list.append("king bed count is empty")
        if not str(data['queen_bed_count']):
            valid_data = False
            message_list.append("queen bed count is empty")
        if not str(data['single_bed_count']):
            valid_data = False
            message_list.append("single bed count is empty")
        if not str(data['bath_room_count']):
            valid_data = False
            message_list.append("bathroom count is empty")

        # Check if room_type_tlt contain  
        # only alphabetic characters (and may be certain special characters)
        if not self.validator.is_alphabetic(data['room_type_tlt']):
            valid_data = False
            message_list.append("invalid room type title")
         
        # Check if king_bed_count, queen_bed_count, single_bed_count, bath_room_count contain  
        # only numeric characters (and may be certain special characters)
        if not self.validator.is_numeric(data['king_bed_count']):
            valid_data = False
            message_list.append("invalid king bed count")
        if not self.validator.is_numeric(data['queen_bed_count']):
            valid_data = False
            message_list.append("invalid queen bed count")
        if not self.validator.is_numeric(data['single_bed_count']):
            valid_data = False
            message_list.append("invalid single bed count")
        if not self.validator.is_numeric(data['bath_room_count']):
            valid_data = False
            message_list.append("invalid bathroom count")
                   
        # Join the items in the list as a string separated with a comma and a space    
        message = ', '.join(message_list) 

        return valid_data, message # return 2 values

# ###########
# Main method
# ###########

if __name__ == '__main__':
    """The main method is only executed when the file is 'run' (not imported in another file)"""
     
    # Setup a root window (in the middle of the screen)
    root = tk.Tk()
    root.title("Room Type System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = RoomTypeGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)
    gui.load()

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass