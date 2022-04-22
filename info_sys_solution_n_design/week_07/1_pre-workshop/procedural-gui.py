# France Cheong
# 22/11/2018

# Step 1. Import the tkinter package
import tkinter as tk

# Step 2. Instantiate the main/root window
# Set its title, its size: width = 350 pixels, height = 200 pixels
root = tk.Tk()
root.title("Welcome to ISYS2047!")
root.geometry('350x200')
 
# Step 3. Create GUI elements/widgets
# First widget
# Instantiate a Label and set its position on the window  
lbl = tk.Label(root, text="Hello") # first parameter is the window that was created
lbl.grid(row=0, column=0) # top left position
 
# Create next widget, etc
# Instantiate a Button and set its position on the window  
btn = tk.Button(root, text="Click Me") # first parameter is the window that was created
btn.grid(row=0, column=1) # to the right of the label

# Step 4. Call the endless window loop to process user inputs
root.mainloop()