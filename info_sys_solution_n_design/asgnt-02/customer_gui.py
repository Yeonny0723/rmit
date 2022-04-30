# customer_gui.py

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox
from tkinter.messagebox import askyesno

from customer_dao import CustomerDAO # To communicate with Customer table
from validation import Validation


# #################
# CustomerGUI Class
# #################

class CustomerGUI():
    """CustomerGUI class to implement CRUD functionalities & methods to manage the user interface"""

    def __init__(self):   
        """Initialiser"""
        # Instantiate a data access object 
        # Contains methods to access the database
        self.customer_dao = CustomerDAO()

        # Instantiate a validation object
        # Contains methods to validate input fields
        self.validator = Validation()

        # Form fields
        # Instantiate stringvars - hold  data entered in  fields of form
        self.customer_id = tk.StringVar()
        self.first_name = tk.StringVar()
        self.lastname = tk.StringVar()
        self.phone_num = tk.StringVar()
        self.email = tk.StringVar()
        self.credit_card_num = tk.StringVar()
        self.expiry_date = tk.StringVar()
        self.cvc_code = tk.StringVar()
        self.dob = tk.StringVar()

        # List of customer ids - lb for listbox
        self.lb_ids = None

        # search
        self.search_lastname = None
        # search list
        self.ln_ids = None

        # Messagebox title
        self.mb_title_bar = "Customer CRUD"

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
        print("\nCreating customer GUI ...")

        # customer_frame = tk.Frame(root).pack() 
        # cannot write the above as pack() does not return anything
        # and need the variable name to refer to it elsewhere
        # DO NOT SPECIFY ANY WIDTH AND HEIGHT OF THE FRAMES 
        # HERE FOR FLEXIBILITY REASONS
        # The height and width or the root window can be specified 
        # in the main GUI (or in the main() method)
        customer_frame = tk.Frame(root)
        customer_frame.pack()

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
        form_frame = tk.Frame(customer_frame)
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
            text = "Customer details").grid(row=0, column=0, columnspan=3)

        # row 1. customer_id label, customer_id entry and list_of_ids label
        tk.Label(
            form_frame, 
            text= "Customer Id", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=1, column=0)
    
        tk.Entry(
            form_frame, 
            textvariable=self.customer_id, 
            width=30, 
            bd=1, 
            state=tk.DISABLED).grid(row=1, column=1)

        # customer_id is disabled to prevent user from entering a value
        # customer_id is generated by the database because AUTOINCREMENT 
        # was specified in the database schema
        tk.Label(
            form_frame, 
            text= "Customer IDs", 
            font=('arial', 10)).grid(row=1, column=2)
        
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


        # ***search by lastname
        tk.Label(
            form_frame, 
            text= "Search by lastname", 
            font=('arial', 10)).grid(row=7, column=2)
        self.search_lastname = tk.Entry(form_frame)
        self.search_lastname.grid(row=8, column=2)

        # row 2. first_name label, first_name entry and listbox of ids
        tk.Label(
            form_frame, 
            text= "First name", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=2, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.first_name, 
            width=30, 
            bd=1).grid(row=2, column=1)

        # row 3: lastname label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Last name", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=3, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.lastname, 
            width=30, 
            bd=1).grid(row=3, column=1)

        # row 4: phone number label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Mobile", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=4, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.phone_num, 
            width=30, 
            bd=1).grid(row=4, column=1)

        # row 5: email address label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Email address", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=5, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.email, 
            width=30, 
            bd=1).grid(row=5, column=1)

        # row 6: credit card number label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Credit card number", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=6, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.credit_card_num, 
            width=30, 
            bd=1).grid(row=6, column=1)

        # row 7: expiry date label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Expiry date (mm/yy)", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=7, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.expiry_date, 
            width=30, 
            bd=1).grid(row=7, column=1)

        # row 8: CVC code label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "CVC code", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=8, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.cvc_code, 
            width=30, 
            bd=1).grid(row=8, column=1)

        # row 9: Date of birth label and entry (the listbox will go through)
        tk.Label(
            form_frame, 
            text= "Date of birth (dd/mm/yyyy)", 
            font=('arial', 10), 
            width=20, 
            anchor="e", 
            bd=1, 
            pady=10, 
            padx=10).grid(row=9, column=0)
        tk.Entry(
            form_frame, 
            textvariable=self.dob, 
            width=30, 
            bd=1).grid(row=9, column=1)

        # Buttons
        # There are 3 columns of widgets in the frame and 4 buttons
        # Better insert the button in another frame
        # Also easier to pack them from the left than using a grid with row 
        # and col locations
        # pady to leave a space from frame on top
        button_frame = tk.LabelFrame(customer_frame, pady=10, text="Commands") 
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
            relief="raised",
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
            command=self.filter_by_lastname).pack(side=tk.LEFT)       

        # Return a reference to the high level frame created
        # Will need the reference to be able to destroy it in the calling function
        return customer_frame

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
    
    def clear_fields(self):
        """Clear the fields of the form"""

        print("\nClearing fields ...")

        # Just blank all the fields
        self.customer_id.set("")
        self.first_name.set("")
        self.lastname.set("")
        self.phone_num.set("")
        self.email.set("")
        self.credit_card_num.set("")
        self.expiry_date.set("")
        self.cvc_code.set("")
        self.dob.set("")

    def save(self):
        """Save the data displayed on the form to the database."""


        print("\nSaving a customer ...")

        # Get the data
        data = self.get_fields()   

        # Validate the data
        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (len(data['customer_id'])==0):
                # If nothing has been entered in customer_id 
                # i.e. its length is zero characters
                print("Calling create() as customer_id is absent")
                self.create(data)
            else:
                print("Calling update() as customer_id is present")
                self.update(data)
                pass
        else:
            message_text = "Invalid fields.\n" + message 
            messagebox.showwarning(self.mb_title_bar, message_text, icon="warning")
            pass

        self.load()

    def get_fields(self):
        """Get the data entered in the fields of the form"""

        print("\nGetting fields ...")

        customer = {}
        # customer_id is ignored when creating a record
        customer['customer_id'] = self.customer_id.get() 
        customer['first_name'] = self.first_name.get()
        customer['lastname'] = self.lastname.get()
        customer['phone_num'] = self.phone_num.get()
        customer['email'] = self.email.get()
        customer['credit_card_num'] = self.credit_card_num.get()
        customer['expiry_date'] = self.expiry_date.get()
        customer['cvc_code'] = self.cvc_code.get()
        customer['dob'] = self.dob.get()

        print(f"customer: {customer}")
 
        return customer    

    def create(self, data):
        """Create a new record in the database"""

        print("\nCreating a customer ...")
        print(f"data: {data}")

        result = self.customer_dao.create(data)

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

        print("\nUpdating a customer ...")
        print(f"data: {data}")

        result = self.customer_dao.update(data['customer_id'], data)

        # Display the returned message to the user - use a messagebox  
        # Display everything that is returned in the result      
        messagebox.showinfo(self.mb_title_bar, result)
        self.load()

    def delete(self):
        """Delete a record from the database"""

        print("\nDeleting  a customer ...")
        
        # Grab the customer_id from the stringvar
        id = self.customer_id.get() 
        print(f"id: {id}")
        
        # Call the data access object to do the job
        # Pass the id as parameter to the delete() method
        result = self.customer_dao.delete(id)   

        # Display the returned message to the user - use a messagebox    
        # Display everything that is returned in the result    
        messagebox.showinfo(self.mb_title_bar, result)
        self.load()

    def load(self):
        """Retrieve a list of IDs from the database and load them into a listbox"""

        print("\nLoading IDs in list box ...")

        result = self.customer_dao.find_ids()
        print(f"result: {result}")

        # Check if there is an entry in the result dictionary
        if "customer_ids" in result: 
            list_ids = result['customer_ids'] # will crash if there is no entry!
            # Set the returned list into the listbox
            # Before doing that, must clear any previous list in the box
            self.lb_ids.delete(0,tk.END)
            print("Setting customer_ids in listbox ...")
            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
                #print(x)
            pass

    def filter_by_lastname(self):
        """Retrieve a list of filtered IDs from the database and load them into a listbox"""

        print("\nLoading filtered IDs in list box ...")

        lastname = self.search_lastname.get()
        result = self.customer_dao.find_by_lastname(lastname)

        if "filtered_customers_ids" in result: 
            list_ids = result['filtered_customers_ids'] # will crash if there is no entry!
            # Set the returned list into the listbox
            # Before doing that, must clear any previous list in the box
            self.lb_ids.delete(0,tk.END)
            print("Setting filtered_customers_ids in listbox ...")
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
          
         # value of the item clicked, in our case it's the customer_id  
        value = w.get(index) 
         
        print(f"index: {index}") 
        print(f"value: {value}")

        # Call find_by_id and populate the stringvars of the form
        result = self.customer_dao.find_by_id(value)

        # { "customer" : {"customer_id": "", "first_name": "", etc}}
        print(f"result: {result}") 

        # Grab customer dict from result dict and use it to populate the fields on the form  
        customer = result['customer_id']
        self.populate_fields(customer)

    def populate_fields(self, customer):
        """Populate the fields of the form with data"""

        print("\nPopulating fields ...")
        print(f"customer: {customer}")

        # Set the values from the dict to the stringvars
        self.customer_id.set(customer['customer_id'])
        self.first_name.set(customer['first_name'])
        self.lastname.set(customer['lastname'])
        self.phone_num.set(customer['phone_num'])
        self.email.set(customer['email'])
        self.credit_card_num.set(customer['credit_card_num'])
        self.expiry_date.set(customer['expiry_date'])
        self.cvc_code.set(customer['cvc_code'])
        self.dob.set(customer['dob'])

    def validate_fields(self, data):
        """Validate the data entered in the fields of the form"""

        print("\nValidating the data ...")
        print(f"data: {data}")
           
        # By default set to true, anything wrong will turn it to false   
        valid_data = True 
        # Instantiate an empty list to contain the messages
        message_list = [] 
        
        # Check for blank fields
        # Do not check customer as this is generated by the database
        if not str(data['first_name']):
            valid_data = False
            message_list.append("firstname is empty")

        if not str(data['lastname']):
            valid_data = False
            message_list.append("lastname is empty")

        if not str(data['phone_num']):
            valid_data = False
            message_list.append("phone number is empty")

        if not str(data['email']):
            valid_data = False
            message_list.append("email is empty")

        if not str(data['credit_card_num']):
            valid_data = False
            message_list.append("credit card number is empty")

        if not str(data['expiry_date']):
            valid_data = False
            message_list.append("expiry date is empty")

        if not str(data['cvc_code']):
            valid_data = False
            message_list.append("cvc code is empty")

        if not str(data['dob']):
            valid_data = False
            message_list.append("Date of birth is empty")


        # Check if firstname and lastname contain  
        # only alphabetic characters (and may be certain special characters)
        if not self.validator.is_alphabetic(data['first_name']):
            valid_data = False
            message_list.append("invalid firstname")

        if not self.validator.is_alphabetic(data['lastname']):
            valid_data = False
            message_list.append("invalid lastname")

        # check if cvc_code contain only numeric digits
        if not self.validator.is_numeric(data['cvc_code']):
            valid_data = False
            message_list.append("invalid cvc code")

        # Check if work_phone follows a certain pattern 
        # i.e. 04xx xxx xxx or 04xx-xxx-xxx
        if not self.validator.is_phone_number(data['phone_num']):
            valid_data = False
            message_list.append("invalid phone number format")
    
        # Check if email follows a certain pattern 
        # i.e contains an @ followed by a dot
        if not self.validator.is_email(data['email']):
            valid_data = False
            message_list.append("invalid email format")

        # Check if credit card number follows a certain pattern 
        # i.e xxxx-xxxx-xxxx-xxxx or xxxx xxxx xxxx xxxx
        if not self.validator.is_credit_num(data['credit_card_num']):
            valid_data = False
            message_list.append("invalid credit card number format")

        # Check if expiry date follows a certain pattern (mm/yy)
        if not self.validator.is_expiry_date(data['expiry_date']):
            valid_data = False
            message_list.append("invalid expiry date format")

        # Check if date of borth follows a certain pattern
        # (dd/mm/yyyy)
        if not self.validator.is_date(data['dob']):
            valid_data = False
            message_list.append("invalid date of birth format")
                   
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
    root.title("Customer System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = CustomerGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)
    gui.load()

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass