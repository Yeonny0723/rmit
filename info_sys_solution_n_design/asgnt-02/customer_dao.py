# customer_dao.py
 
# Import packages
import sqlite3

# Constants
DATABASE_URI = "ahs_reservation.db"

class CustomerDAO():
    """CustomerDAO class to perform CRUD operations on the customer table in the database"""
    
    def create(self, data):
        """
        Create/insert a record in a table

        Parameters: data input

        Return: data insertion result
        """
        # Print info for debugging
        print("\nCreating a customer ...\n") #\n means print("\n") a blank line
        print(f"data: {data}")

        result = {}

        # Parameterized Query i.e. question marks as placeholders for  actual values
        conn = None # First initialise the connection to None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);" # all columns + PK
            param_tuple = (
                None, # customer_id is set to None for database to autoincrement
                data['first_name'], 
                data['lastname'],
                data['phone_num'],
                data['email'],
                data['credit_card_num'],
                data['expiry_date'],
                data['cvc_code'],
                data['dob']
            )    
            cur.execute(query, param_tuple)
            result['message'] = 'Customer added successfully!' 

            # OPTIONAL: Get the id of record inserted - cursor should be still open
            # Might be useful later in more advanced cases
            # e.g. when inserting records in 2 tables at the same time for 1:m transactions
            inserted_customer_id = cur.lastrowid
            print(f"inserted_customer_id: {inserted_customer_id}")
            result['customer_id'] = inserted_customer_id

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            # This part of the code is executed if an error occured when executing any statement in the try block
            result['message'] = 'Create customer failed!' 
            print(f"Database {DATABASE_URI} - Create customer failed!")
            print(error)
        finally:
            # The finally block is always executed - even if an exception happened
            # This is the ideal place to close the connection
            # It's always a good idea to check if the object exists before calling a method/function from the object
            # Invoking a method on object which does not exist will cause your code to crash
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary  

    def find_by_id(self, customer_id):
        """
        Find a record by id

        Parameters: customer id 

        Return: data search result
        """
        
        # Print info for debugging
        print("\nFinding a customer ...\n")
        print(f"customer_id: {customer_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.row_factory = sqlite3.Row # to be able to use row.keys()
            cur = conn.cursor()
            query = "SELECT * FROM customer WHERE customer_id=?;"
            param_tuple = (customer_id, ) # Works as this is a tuple of length 1
            cur.execute(query, param_tuple)
            row = cur.fetchone() # get the next row - only one row in this case
            if row:
                # cursor.description contains the name of the columns
                # Use dictionary compejension to build the dictionary
                # Use list comprehension - get column names from cursor.description
                # The column name is at index 0 i.e. the first position
                col_names = [description[0] for description in cur.description]
                #print(f"Column names: {col_names}")
                # Using dictionary comprehension and enumerate() 
                #   to match the column names with their index positions
                d = {key: row[i] for i, key in enumerate(col_names)}
                result['customer_id'] = d
            else:    
                result['message'] = "Customer not found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by id failed!' 
            print(f"Database {DATABASE_URI} - Find by id failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        # Note that the return is not part of the if/else block
        # Ensure it's indented to the left
        #print(f"result: {result}")
        return result # return the result as a dictionary

    def find_by_lastname(self, lastname):
        """
        Filter customer records by customer lastname

        Parameters: customer lastname

        Return: data search result
        """
        # Print info for debugging
        print("\nFinding customer(s) by lastname ...\n")
        if lastname:
            print(f"lastname: {lastname}")
        else:
            print("no text input")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM customer WHERE lastname LIKE ?;" # Partial match
            # query = "SELECT * FROM customer WHERE lastname = ?;" # Exact match
            param_tuple = (lastname, ) # If a single value, must have a comma at the end!
            cur.execute(query, param_tuple)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one customers - so create a list
                list_customers_id = [] # Create an empty list to append customer dicts
                for x in rows: # rows is a list of SQlite objects - process one by one
                    list_customers_id.append(x[0])
                      
                # Store the customer list in the result dict under key "customers"              
                result['filtered_customers_ids'] = list_customers_id                

            else:    
                result['message'] = "No customers found!"
                result['filtered_customers_ids'] = []                

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by lastname failed!' 
            print(f"Database {DATABASE_URI} - Find by lastname failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")   
        return result  # return the result as a dictionary   

    def find_all(self):
        """
        Find all customer records

        Parameters: None

        Return: data search result
        """
        # Print info for debugging
        print("\nFinding all customers ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM customer;"
            #param_tuple = ()
            #cur.execute(query, param_tuple)
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one customers - so create a list
                list_customers = [] # Create an empty list to append customer dicts
                for x in rows: # rows is a list of SQLite objects - process one by one
                    # cursor.description contains the name of the columns
                    # Use dictionary comprehension to build the dictionary
                    # Use list comprehension - get column names from cursor.description
                    # The column name is at index 0 i.e. the first position
                    col_names = [description[0] for description in cur.description]
                    #print(f"Column names: {col_names}")
                    # Using dictionary comprehension and enumerate() 
                    #   to match the column names with their index positions
                    d = {key: x[i] for i, key in enumerate(col_names)} # works

                    list_customers.append(d) # Append the customer dict to the customer list
                    pass     

                # After the for loop
                # Store customer list in result dict under key "customers" - PLURAL             
                result['customers'] = list_customers    
            else:    
                result['message'] = "No customers found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find all failed!' 
            print(f"Database {DATABASE_URI} - Find all failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")    
        return result # return the result as a dictionary

    def find_ids(self):
        """
        This is a special method similar to find_all but returns customer_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all customers ids ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT customer_id FROM customer;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                result['customer_ids'] = [x[0] for x in rows] # List comprehension to grab first element of the tuple
            else:    
                result['message'] = "No customers found!"
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find ids failed!' 
            print(f"Database {DATABASE_URI} - Find ids failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}") 
        return result # return the result as a dictionary

    def update(self, customer_id, data):
        """
        Updating one record from a table

        Parameters: customer id to be changed

        Return: data insertion result
        """

        # Print info for debugging
        print("\nUpdating customer ...\n")
        print(f"customer_id: {customer_id}")
        print(f"data: {data}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # Update all the attributes in customer table except customer_id
            query = """UPDATE customer
               SET 
                  first_name=?, 
                  lastname=?,
                  phone_num=?,
                  email=?,
                  credit_card_num=?,
                  expiry_date=?,
                  cvc_code=?,
                  dob=?
              WHERE 
                  customer_id = ?;"""
            param_tuple = (
                data['first_name'], 
                data['lastname'], 
                data['phone_num'], 
                data['email'], 
                data['credit_card_num'], 
                data['expiry_date'], 
                data['cvc_code'], 
                data['dob'], 
                customer_id)
            cur.execute(query, param_tuple)
            result['message'] = 'Customer Updated!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Customer NOT updated!' 
            print(f"Database {DATABASE_URI} - Update Customer failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result

    def delete(self, customer_id):
        """
        Deleting one record from a table

        Parameters: customer id to be deleted

        Return: data deletion result
        """

        # Print info for debugging
        print("\nDeleting customer ...\n")
        print(f"customer_id: {customer_id}")
 
        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.execute("PRAGMA foreign_keys = 1")
            cur = conn.cursor()
            query = "DELETE FROM customer WHERE customer_id = ?;"
            param_tuple = (customer_id, )
            cur.execute(query, param_tuple)
            result['message'] = 'Customer deleted!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Customer NOT deleted!' 
            print(f"Database {DATABASE_URI} - Delete customer failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary    
