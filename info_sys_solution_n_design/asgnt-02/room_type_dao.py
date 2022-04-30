# room_type_dao.py
 
# Import packages
import sqlite3

# Constants
DATABASE_URI = "ahs_reservation.db"

class RoomTypeDAO():
    """RoomTypeDAO class to perform CRUD operations on the room type table in the database"""

    def create(self, data):
        """
        Create/insert a record in a table

        Parameters: data input

        Return: data insertion result
        """
        # Print info for debugging
        print("\nCreating a room type ...\n") #\n means print("\n") a blank line
        print(f"data: {data}")

        result = {}

        # Parameterized Query i.e. question marks as placeholders for  actual values
        conn = None # First initialise the connection to None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "INSERT INTO room_type VALUES (?, ?, ?, ?, ?, ?);" # all columns + PK
            param_tuple = (
                None, # staff_id is set to None for database to autoincrement
                data['room_type_tlt'], 
                data['king_bed_count'],
                data['queen_bed_count'],
                data['single_bed_count'],
                data['bath_room_count']
            )    
            cur.execute(query, param_tuple)
            result['message'] = 'Room type added successfully!' 

            # OPTIONAL: Get the id of record inserted - cursor should be still open
            # Might be useful later in more advanced cases
            # e.g. when inserting records in 2 tables at the same time for 1:m transactions
            inserted_room_type_id = cur.lastrowid
            print(f"inserted_room_type_id: {inserted_room_type_id}")
            result['room_type_id'] = inserted_room_type_id

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            # This part of the code is executed if an error occured when executing any statement in the try block
            result['message'] = 'Create room type failed!' 
            print(f"Database {DATABASE_URI} - Create oom type failed!")
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

    def find_by_id(self, room_type_id):
        """
        Find a record by id

        Parameters: room type id 

        Return: data search result
        """
        
        # Print info for debugging
        print("\nFinding a room type ...\n")
        print(f"room_type_id: {room_type_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.row_factory = sqlite3.Row # to be able to use row.keys()
            cur = conn.cursor()
            query = "SELECT * FROM room_type WHERE room_type_id=?;"
            param_tuple = (room_type_id, ) # Works as this is a tuple of length 1
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
                result['room_type'] = d
            else:    
                result['message'] = "Room type not found!"
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

    def find_by_room_type(self, room_type_tlt):
        """
        Filter room type by room type title

        Parameters: room type title

        Return: data search result
        """

        # Print info for debugging
        print("\nFinding room_type(s) by room_type_tlt ...\n")
        if room_type_tlt:
            print(f"room_type_tlt: {room_type_tlt}")
        else:
            print("no text input")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM room_type WHERE room_type_tlt LIKE ?;" # Partial match
            # query = "SELECT * FROM room_type WHERE room_type_tlt = ?;" # Exact match
            param_tuple = (room_type_tlt, ) # If a single value, must have a comma at the end!
            cur.execute(query, param_tuple)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one room_type - so create a list
                list_room_types_id = [] # Create an empty list to append room_type dicts
                for x in rows: # rows is a list of SQlite objects - process one by one
                    list_room_types_id.append(x[0])
                      
                # Store the room_type list in the result dict under key "room_types"              
                result['filtered_room_types_ids'] = list_room_types_id                

            else:    
                result['message'] = "No room_types found!"
                result['bookings'] = []
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by room_type_tlt failed!' 
            print(f"Database {DATABASE_URI} - Find by room_type_tlt failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")   
        return result  # return the result as a dictionary   

    def find_all(self):
        """
        Find all room type records

        Parameters: None

        Return: data search result
        """
        # Print info for debugging
        print("\nFinding all room types ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM room_type;"
            #param_tuple = ()
            #cur.execute(query, param_tuple)
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one room_types - so create a list
                list_room_types = [] # Create an empty list to append room_type dicts
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

                    list_room_types.append(d) # Append the room_types dict to the room_types list
                    pass     

                # After the for loop
                # Store room_types list in result dict under key "room_types" - PLURAL             
                result['room_types'] = list_room_types    
            else:    
                result['message'] = "No room_types found!"
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
        This is a special method similar to find_all but returns room_type_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all room type ids ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT room_type_id FROM room_type;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                result['room_type_ids'] = [x[0] for x in rows] # List comprehension to grab first element of the tuple
            else:    
                result['message'] = "No room types found!"
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

    def update(self, room_type_id, data):
        """
        Updating one record from a table

        Parameters: room type id to be changed

        Return: data insertion result
        """

        # Print info for debugging
        print("\nUpdating room type ...\n")
        print(f"room_type_id: {room_type_id}")
        print(f"data: {data}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # Update all the attributes in room type table except room_type_id
            query = """UPDATE room_type
               SET 
                  room_type_tlt=?, 
                  king_bed_count=?,
                  queen_bed_count=?,
                  single_bed_count=?,
                  bath_room_count=?
              WHERE 
                  room_type_id = ?;"""
            param_tuple = (
                data['room_type_tlt'], 
                data['king_bed_count'], 
                data['queen_bed_count'], 
                data['single_bed_count'], 
                data['bath_room_count'], 
                room_type_id)
            cur.execute(query, param_tuple)
            result['message'] = 'room type Updated!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'room type NOT updated!' 
            print(f"Database {DATABASE_URI} - Update room type failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result

    def delete(self, room_type_id):
        """
        Deleting one record from a table

        Parameters: room type id to be deleted

        Return: data deletion result
        """

        # Print info for debugging
        print("\nDeleting room type ...\n")
        print(f"room_type_id: {room_type_id}")
 
        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.execute("PRAGMA foreign_keys = 1")
            cur = conn.cursor()
            query = "DELETE FROM room_type WHERE room_type_id = ?;"
            param_tuple = (room_type_id, )
            cur.execute(query, param_tuple)
            result['message'] = 'room type deleted!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'room type NOT deleted!' 
            print(f"Database {DATABASE_URI} - Delete room type failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary    

