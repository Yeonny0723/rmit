# oop-gui.py
# France Cheong
# 22/11/2018

# Step 1. Import the tkinter package
import tkinter as tk

class MyGUI():
    """
    The GUI is defined as a class
    """
    # If the returned value (the frame created) is not needed
    # Then, could write the content of create_gui() in __init__
    # __init__does not return any value
    def create_gui(self, root):
        """
        Create a high level frame which contains the entire GUI
        and adds it to the root window (passed as second parameter)

        Widgets like labels, entries, etc are added to the high level frame 
        At the end, return a reference to the frame that was created 
        for the calling program to be able to access it.

        Parameters (apart from self):
            root: main window of application

        Return: 
            my_frame: the frame containing all the widgets 

        """

        # Step 5. Create a frame 
        # and link it to root window passed as parameter
        my_frame = tk.Frame(root)
        # pack the frame to make it visible
        #my_frame.pack() # frame will be centered
        # Fill entire parent and also when user resizes window
        my_frame.pack(fill=tk.BOTH, expand=1) 

        # Step 6. Create GUI elements/widgets
        # First widget
        # Instantiate a Label and set its position on the window  
        # first parameter is frame that was created
        lbl = tk.Label(my_frame, text="Hello")
        lbl.grid(row=0, column=0) # top left position
        
        # Create next widget, etc
        # Instantiate a Button and set its position on the window  
        # first parameter is frame that was created
        btn = tk.Button(my_frame, text="Click Me") 
        btn.grid(row=0, column=1) # to the right of the label
        
        # Step 7. Return a reference to the frame
        return my_frame

# ###########
# Main method
# ###########

if __name__ == '__main__':
    """
    The main method is only executed when the file is 'run' 
    (not imported in another file)
    """
     
    # Step 2. Setup a root window in the main program
    # Set its title, its size: width = 350 pixels, height = 200 pixels
    root = tk.Tk()
    root.title("Welcome to ISYS2047!")
    root.geometry('350x200')

    # Step 3. Instantiate the gui class
    gui = MyGUI()

    # Step 4. Invoke the create_gui() on the object
    # And pass the root window as parameter
    gui.create_gui(root)

    # Step 8. Run the mainloop
    # the endless window loop to process user inputs
    root.mainloop()