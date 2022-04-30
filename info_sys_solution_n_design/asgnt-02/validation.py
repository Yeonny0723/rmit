# validation.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########
from datetime import datetime
import re # regular expression

# ################
# Validation Class
# ################

class Validation():

    def is_numeric(self, val):
        """
        Check if input is numeric

        Parameters: data to be examined

        Return: True/False
        """
        val = str(val) # only str have the isnumeric() method
        if val.isnumeric(): 
            print("Int") # 12
            return True
        elif val.replace('.','').isnumeric():
            print("Float") # 12.2
            return True
        else:
            print("Not numeric")
            return False 

    def is_alphabetic(self, val):
        """
        Check if input contains only alphabet

        Parameters: data to be examined

        Return: True/False
        """
        val = str(val)
        if val.isalpha():
            print("Alphabetic")
            return True
        else:
            print("Not alphabetic")
            return False  

    def is_phone_number(self, val):
        """
        Check if input phone follows the following format
        xxxx xxx xxx or xxxx-xxx-xxx

        Parameters: data to be examined

        Return: True/False
        """
        val = str(val)
        if re.search(r'(^\d{4} \d{3} \d{3})', val): # 0423 999 999
            print("Valid phone number")
            return True
        elif re.search(r'(^\d{4}-\d{3}-\d{3})', val): # 0423 999 999
            print("Valid phone number")
            return True
        else:
            print("Invalid phone number")
            return False  

    def is_email(self, val):
        """
        Check if input follows the following format:
        xxxx@xxx

        Parameters: data to be examined

        Return: True/False
        """
        val = str(val)
        # Check that it has exactly one @ sign, 
        # and at least one . in the part after the @
        if re.match(r'[\w.-]+@[\w.-]+', val):
        #if re.search(r'\w+@\w+', val):
            print("Valid email")
            return True
        else:
            print("Invalid email")
            return False  

    def is_date(self, val):
        """
        Check if input phone follows the following format
        dd/mm/yyyy

        Parameters: data to be examined

        Return: True/False
        """
        val = str(val)
        # check if the date follows the written format
        format = "%d/%m/%Y" # 23/07/1999
        res = False
        try:
            res = bool(datetime.strptime(val, format))
        except ValueError:
            res = False
        if res:
            print("Valid date format")
        else:
            print("Invalid date format")
        return res 

    def is_expiry_date(self, val):
        """
        Check if input phone follows the following format
        mm/yy/

        Parameters: data to be examined

        Return: True/False
        """
        val = str(val)
        format = "%m/%y" # 12/23
        res = None
        try:
            res = bool(datetime.strptime(val, format))
        except ValueError:
            res = False
        if res:
            print("Valid date format")
        else:
            print("Invalid date format")
        return res   

    def is_credit_num(self, val):
        """
        Check if input phone follows the following format
        xxxx xxxx xxxx xxxx or xxxx-xxxx-xxxx-xxxx

        Parameters: data to be examined

        Return: True/False
        """
        val = str(val)
        if re.match('(^\d{4} \d{4} \d{4} \d{4})', val): # 1234 5678 9012 3456
            print("Valid credit card format")
            return True
        elif re.match('(^\d{4}-\d{4}-\d{4}-\d{4})', val): # 1234-5678-9012-3456
            print("Valid credit card format")
            return True
        else:
            print("Invalid credit card format")
            return False
    pass

# ###########
# Main method
# ###########

# The main method is only executed when the file is 'run' (not imported in another file)

if __name__ == '__main__':
    # Instead of writing separate test scripts, could write them here
    # The test scripts would not be executed when the file is imported into another one
    pass        