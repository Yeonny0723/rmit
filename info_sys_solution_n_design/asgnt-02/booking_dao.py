# booking_dao.py
 
# Import packages
import sqlite3
from datetime import datetime

# Constants
DATABASE_URI = "ahs_reservation.db"

class BookingDAO():
    """BookingDAO class to perform CRUD operations on the booking table in the database"""

    def create(self, data):
        """
        Create/insert a record in a table

        Parameters: data input

        Return: data insertion result
        """

        # Print info for debugging
        print("\nCreating a booking ...\n") #\n means print("\n") a blank line
        print(f"data: {data}")

        result = {}

        # Parameterized Query i.e. question marks as placeholders for  actual values
        conn = None # First initialise the connection to None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "INSERT INTO booking VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);" # all columns + PK
            param_tuple = (
                None, # booking_id is set to None for database to autoincrement
                data['check_in'], 
                data['check_out'],
                data['extra_bed'],
                data['adult_num'],
                data['child_num'],
                data['infant_num'],
                data['total_price'],
                data['booking_dtm'],
                data['room_id'],
                data['staff_id'],
                data['customer_id'],
                data['phone_num']
            )    
            cur.execute(query, param_tuple)
            result['message'] = 'booking added successfully!' 

            # OPTIONAL: Get the id of record inserted - cursor should be still open
            # Might be useful later in more advanced cases
            # e.g. when inserting records in 2 tables at the same time for 1:m transactions
            inserted_booking_id = cur.lastrowid
            print(f"inserted_booking_id: {inserted_booking_id}")
            result['booking_id'] = inserted_booking_id

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            # This part of the code is executed if an error occured when executing any statement in the try block
            result['message'] = 'Create booking failed!' 
            print(f"Database {DATABASE_URI} - Create booking failed!")
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

    def find_by_id(self, booking_id):
        """
        Find a record by id

        Parameters: booking id 

        Return: data search result
        """

        # Print info for debugging
        print("\nFinding a booking ...\n")
        print(f"booking_id: {booking_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.row_factory = sqlite3.Row # to be able to use row.keys()
            cur = conn.cursor()
            query = "SELECT * FROM booking WHERE booking_id=?;"
            param_tuple = (booking_id, ) # Works as this is a tuple of length 1
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
                result['booking'] = d
            else:    
                result['message'] = "booking not found!"
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

    def find_by_customer_id(self, customer_id):
        """
        Filter booking records by customer id

        Parameters: customer id 

        Return: data search result
        """
        
        # Print info for debugging
        print("\nFinding booking(s) by customer_id ...\n")
        print(f"customer_id: {customer_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # query = "SELECT * FROM booking WHERE customer_id LIKE ?;" # Partial match
            query = "SELECT * FROM booking WHERE customer_id = ?;" # Exact match
            param_tuple = (customer_id, ) # If a single value, must have a comma at the end!
            cur.execute(query, param_tuple)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one booking - so create a list
                list_bookings = [] # Create an empty list to append booking dicts
                for x in rows: # rows is a list of SQlite objects - process one by one
                    list_bookings.append(x[0])
                # Store the booking list in the result dict under key "booking"  
                result['filtered_booking_ids'] = list_bookings                

            else:    
                result['message'] = "No bookings found!"
                result['filtered_booking_ids'] = []  

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by customer_id failed!' 
            print(f"Database {DATABASE_URI} - Find by customer_id failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")   
        return result  # return the result as a dictionary   

    def find_all(self):
        """
        Find all booking records

        Parameters: None

        Return: data search result
        """
        
        # Print info for debugging
        print("\nFinding all bookings ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM booking;"
            #param_tuple = ()
            #cur.execute(query, param_tuple)
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one bookings - so create a list
                list_bookings = [] # Create an empty list to append bookings dicts
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

                    list_bookings.append(d) # Append the bookings dict to the bookings list
                    pass     

                # After the for loop
                # Store bookings list in result dict under key "bookings" - PLURAL             
                result['bookings'] = list_bookings    
            else:    
                result['message'] = "No bookings found!"
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
        This is a special method similar to find_all but returns booking_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all booking ids ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT booking_id FROM booking;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                result['booking_ids'] = [x[0] for x in rows] # List comprehension to grab first element of the tuple
            else:    
                result['message'] = "No bookings found!"
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

    def update(self, booking_id, data):
        """
        Updating one record from a table

        Parameters: booking id to be changed

        Return: data insertion result
        """
        # Print info for debugging
        print("\nUpdating booking ...\n")
        print(f"booking_id: {booking_id}")
        print(f"data: {data}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # Update all the attributes in booking table except booking_id
            query = """UPDATE booking
               SET 
                  check_in=?, 
                  check_out=?,
                  extra_bed=?,
                  adult_num=?,
                  child_num=?,
                  infant_num=?,
                  booking_dtm=?,
                  room_id=?,
                  staff_id=?,
                  customer_id=?,
                  phone_num=?
              WHERE 
                  booking_id = ?;"""
            param_tuple = (
                data['check_in'], 
                data['check_out'], 
                data['extra_bed'], 
                data['adult_num'], 
                data['child_num'], 
                data['infant_num'], 
                data['booking_dtm'], 
                data['room_id'], 
                data['staff_id'], 
                data['customer_id'], 
                data['phone_num'], 
                booking_id)
            cur.execute(query, param_tuple)
            result['message'] = 'booking Updated!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'booking NOT updated!' 
            print(f"Database {DATABASE_URI} - Update booking failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result

    def delete(self, booking_id):
        """
        Deleting one record from a table

        Parameters: booking id to be deleted

        Return: data deletion result
        """

        # Print info for debugging
        print("\nDeleting booking ...\n")
        print(f"booking_id: {booking_id}")
 
        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.execute("PRAGMA foreign_keys = 1")
            cur = conn.cursor()
            query = "DELETE FROM booking WHERE booking_id = ?;"
            param_tuple = (booking_id, )
            cur.execute(query, param_tuple)
            result['message'] = 'booking deleted!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'booking NOT deleted!' 
            print(f"Database {DATABASE_URI} - Delete booking failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary    

    def retrieve_data(self, db_name):
        """
        Retrieve all records of specified db

        Parameters: database name you want to retrieve

        Return: all PK(id) retrieved from db
        """

        # Open a connection
        conn = sqlite3.connect(DATABASE_URI)
        print(f"Opened a connection to database {DATABASE_URI}")

        with conn:
            # Get a cursor
            cur = conn.cursor()
            DATA_RETRIEVE_SQL = f"select * from {db_name}"
            # Create the customer table
            cur.execute(DATA_RETRIEVE_SQL)
            fetched_df = cur.fetchall()
            return fetched_df

    def get_room_price(self, room_id):
        """
        Retrieve room price with specific room id

        Parameters: room id

        Return: room price
        """

        # Open a connection
        conn = sqlite3.connect(DATABASE_URI)
        print(f"Opened a connection to database {DATABASE_URI}")

        with conn:
            # Get a cursor
            cur = conn.cursor()
            DATA_RETRIEVE_SQL = f"select * from room where room_id={room_id}"
            # Create the customer table
            cur.execute(DATA_RETRIEVE_SQL)
            fetched_df = cur.fetchall()[0]
            return fetched_df
