# main_gui.py

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox

# #################################################
# Import any of your classes defined in other files
# #################################################

# Import all the GUI classes implementing each menu option

from customer_gui import CustomerGUI
from staff_gui import StaffGUI
from room_type_gui import RoomTypeGUI
from room_gui import RoomGUI
from booking_gui import BookingGUI

# ################
# Global Constants 
# ################


# ####################
# MainGUI Class
# ####################

class MainGUI():

    def __init__(self):   
        """Initialiser"""
        print("Creating Main GUI ...")

        self.current_gui = None # Reference to current GUI 

        # Step 1. Create main window of the application
        # 900x500 pixels in the middle of the screen
        # Can minimise to 0x0 pixels
        self.root = tk.Tk()
        self.root.title("AHS Reservation System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        print("Main window coordinates (width, height, x, y) :", 
              width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        # Step 2. Add a menu

        # Create a toplevel menu
        menubar = tk.Menu(self.root)

        # File menu (pulldown)
        # Create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Main", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Home", menu=filemenu)

        # Customer menu
        # do not use self.create_customer_gui()
        # Will be executed automatically!

        # # If you are using MacOS Monterey, be sure to uncomment the code below. 
        # # customer
        # filemenu = tk.Menu(menubar, tearoff=0)
        # filemenu.add_command(label="Customer", command=self.create_customer_gui)
        # menubar.add_cascade(label="Customer", menu=filemenu)
        # # Staff
        # filemenu = tk.Menu(menubar, tearoff=0)
        # filemenu.add_command(label="Staff", command=self.create_staff_gui)
        # menubar.add_cascade(label="Staff", menu=filemenu)
        # # menubar.add_cascade(label="Staff", command=self.create_staff_gui)
        # # Room Type
        # filemenu = tk.Menu(menubar, tearoff=0)
        # filemenu.add_command(label="Room Type", command=self.create_room_type_gui)
        # menubar.add_cascade(label="Room Type", menu=filemenu)
        # # Room 
        # filemenu = tk.Menu(menubar, tearoff=0)
        # filemenu.add_command(label="Room", command=self.create_room_gui)
        # menubar.add_cascade(label="Room", menu=filemenu)
        # # Booking
        # filemenu = tk.Menu(menubar, tearoff=0)
        # filemenu.add_command(label="Booking", command=self.create_booking_gui)
        # menubar.add_cascade(label="Booking", menu=filemenu)

        # If you are using os other than MacOS Monterey, be sure to uncomment the code below. 
        menubar.add_command(label="Customer", command=self.create_customer_gui)
        menubar.add_command(label="Staff", command=self.create_staff_gui)
        menubar.add_command(label="Room Type", command=self.create_room_type_gui)
        menubar.add_command(label="Room", command=self.create_room_gui)
        menubar.add_command(label="Booking", command=self.create_booking_gui)


        # Display the menu
        self.root.config(menu=menubar)

        pass   
 
    """
    # Beware: There is a built-in function called exit() 
    # with no argument
    def exit(self):
        answer = messagebox.askyesno('Procurement System', 
                    'Are you sure you want to exit?', icon="warning")
        if answer:
            self.root.destroy()
            exit()    
    """        
            
    # Functions to create child frames 
    # when menu options are selected


    def create_customer_gui(self):
        """
        Create the main menu linking to create customer gui.
        The first (and mandatory) parameter to all methods 
        is "self" i.e. a reference to the object instantiated from the class.
        """
        print("\nCreating customer GUI ...")

        # Destroy whatever the current GUI is 
        # and create the customer GUI
        if self.current_gui:
            self.current_gui.destroy()

        customer_gui = CustomerGUI()
        self.current_gui = customer_gui.create_gui(self.root)
        pass
   
    def create_staff_gui(self):
        """
        Create the main menu linking to create staff gui.
        The first (and mandatory) parameter to all methods 
        is "self" i.e. a reference to the object instantiated from the class.
        """
        print("\nCreating staff GUI ...")

        # Destroy whatever the current GUI is 
        # and create the doctor GUI
        if self.current_gui:
            self.current_gui.destroy()

        staff_gui = StaffGUI()
        self.current_gui = staff_gui.create_gui(self.root)
        pass

    def create_room_type_gui(self):
        """
        Create the main menu linking to create room type gui.
        The first (and mandatory) parameter to all methods 
        is "self" i.e. a reference to the object instantiated from the class.
        """
        print("\nCreating room type GUI ...")

        # Destroy whatever the current GUI is 
        # and create the doctor GUI
        if self.current_gui:
            self.current_gui.destroy()

        room_type_gui = RoomTypeGUI()
        self.current_gui = room_type_gui.create_gui(self.root)
        pass

    def create_room_gui(self):
        """
        Create the main menu linking to create room gui.
        The first (and mandatory) parameter to all methods 
        is "self" i.e. a reference to the object instantiated from the class.
        """
        print("\nCreating room GUI ...")

        # Destroy whatever the current GUI is 
        # and create the doctor GUI
        if self.current_gui:
            self.current_gui.destroy()

        room_gui = RoomGUI()
        self.current_gui = room_gui.create_gui(self.root)
        pass

    def create_booking_gui(self):
        """
        Create the main menu linking to create booking gui.
        The first (and mandatory) parameter to all methods 
        is "self" i.e. a reference to the object instantiated from the class.
        """
        print("\nCreating booking GUI ...")

        # Destroy whatever the current GUI is 
        # and create the doctor GUI
        if self.current_gui:
            self.current_gui.destroy()

        booking_gui = BookingGUI()
        self.current_gui = booking_gui.create_gui(self.root)
        pass

# ###########
# Main method
# ###########

if __name__ == '__main__':

    # Instantiate the main application gui 
    # it will create all the necessary GUIs
    gui = MainGUI()

    # Run the mainloop 
    # the endless window loop to process user inputs
    gui.root.mainloop()