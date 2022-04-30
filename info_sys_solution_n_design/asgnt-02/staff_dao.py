# staff_dao.py
 
# Import packages
import sqlite3

# Constants
DATABASE_URI = "ahs_reservation.db"

class StaffDAO():
    """StaffDAO class to perform CRUD operations on the staff table in the database"""
    
    def create(self, data):
        """
        Create/insert a record in a table

        Parameters: data input

        Return: data insertion result
        """
        # Print info for debugging
        print("\nCreating a staff ...\n") #\n means print("\n") a blank line
        print(f"data: {data}")

        result = {}

        # Parameterized Query i.e. question marks as placeholders for  actual values
        conn = None # First initialise the connection to None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "INSERT INTO staff VALUES (?, ?, ?, ?, ?);" # all columns + PK
            param_tuple = (
                None, # staff_id is set to None for database to autoincrement
                data['first_name'], 
                data['lastname'],
                data['email'],
                data['title']
            )    
            cur.execute(query, param_tuple)
            result['message'] = 'Staff added successfully!' 

            # OPTIONAL: Get the id of record inserted - cursor should be still open
            # Might be useful later in more advanced cases
            # e.g. when inserting records in 2 tables at the same time for 1:m transactions
            inserted_staff_id = cur.lastrowid
            print(f"inserted_staff_id: {inserted_staff_id}")
            result['staff_id'] = inserted_staff_id

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            # This part of the code is executed if an error occured when executing any statement in the try block
            result['message'] = 'Create staff failed!' 
            print(f"Database {DATABASE_URI} - Create staff failed!")
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

    def find_by_id(self, staff_id):
        """
        Find a record by id

        Parameters: staff id 

        Return: data search result
        """
        
        # Print info for debugging
        print("\nFinding a staff ...\n")
        print(f"staff_id: {staff_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.row_factory = sqlite3.Row # to be able to use row.keys()
            cur = conn.cursor()
            query = "SELECT * FROM staff WHERE staff_id=?;"
            param_tuple = (staff_id, ) # Works as this is a tuple of length 1
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
                result['staff'] = d
            else:    
                result['message'] = "Staff not found!"
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
        Filter staff records by staff lastname

        Parameters: staff lastname 

        Return: data search result
        """

        # Print info for debugging
        print("\nFinding staff(s) by lastname ...\n")
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
            query = "SELECT * FROM staff WHERE lastname LIKE ?;" # Partial match
            # query = "SELECT * FROM staff WHERE lastname = ?;" # Exact match
            param_tuple = (lastname, ) # If a single value, must have a comma at the end!
            cur.execute(query, param_tuple)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one staff - so create a list
                list_staffs_id = [] # Create an empty list to append staff dicts
                for x in rows: # rows is a list of SQlite objects - process one by one
                    list_staffs_id.append(x[0])
                      
                # Store the staff list in the result dict under key "staffs"              
                result['filtered_staffs_ids'] = list_staffs_id                

            else:    
                result['message'] = "No staffs found!"
                result['bookings'] = []
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
        Find all staff records

        Parameters: None

        Return: data search result
        """
        # Print info for debugging
        print("\nFinding all staffs ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM staff;"
            #param_tuple = ()
            #cur.execute(query, param_tuple)
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one staffs - so create a list
                list_staffs = [] # Create an empty list to append staff dicts
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

                    list_staffs.append(d) # Append the staff dict to the staff list
                    pass     

                # After the for loop
                # Store staff list in result dict under key "staffs" - PLURAL             
                result['staffs'] = list_staffs    
            else:    
                result['message'] = "No staffs found!"
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
        This is a special method similar to find_all but returns staff_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all staff ids ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT staff_id FROM staff;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                result['staff_ids'] = [x[0] for x in rows] # List comprehension to grab first element of the tuple
            else:    
                result['message'] = "No staffs found!"
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

    def update(self, staff_id, data):
        """
        Updating one record from a table

        Parameters: staff id to be changed

        Return: data insertion result
        """

        # Print info for debugging
        print("\nUpdating staff ...\n")
        print(f"staff_id: {staff_id}")
        print(f"data: {data}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # Update all the attributes in staff table except staff_id
            query = """UPDATE staff
               SET 
                  first_name=?, 
                  lastname=?,
                  email=?,
                  title=?
              WHERE 
                  staff_id = ?;"""
            param_tuple = (
                data['first_name'], 
                data['lastname'], 
                data['email'], 
                data['title'], 
                staff_id)
            cur.execute(query, param_tuple)
            result['message'] = 'staff Updated!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'staff NOT updated!' 
            print(f"Database {DATABASE_URI} - Update staff failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result

    def delete(self, staff_id):
        """
        Deleting one record from a table

        Parameters: staff id to be deleted

        Return: data deletion result
        """

        # Print info for debugging
        print("\nDeleting staff ...\n")
        print(f"staff_id: {staff_id}")
 
        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.execute("PRAGMA foreign_keys = 1")
            cur = conn.cursor()
            query = "DELETE FROM staff WHERE staff_id = ?;"
            param_tuple = (staff_id, )
            cur.execute(query, param_tuple)
            result['message'] = 'staff deleted!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'staff NOT deleted!' 
            print(f"Database {DATABASE_URI} - Delete staff failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary    
