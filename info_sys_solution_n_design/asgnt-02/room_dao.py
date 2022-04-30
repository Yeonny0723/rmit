# room_dao.py
 
# Import packages
import sqlite3

# Constants
DATABASE_URI = "ahs_reservation.db"

class RoomDAO():
    """RoomDAO class to perform CRUD operations on the room table in the database"""
    
    def create(self, data):
        """
        Create/insert a record in a table

        Parameters: data input

        Return: data insertion result
        """
        # Print info for debugging
        print("\nCreating a room ...\n") #\n means print("\n") a blank line
        print(f"data: {data}")

        result = {}

        # Parameterized Query i.e. question marks as placeholders for  actual values
        conn = None # First initialise the connection to None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "INSERT INTO room VALUES (?, ?, ?, ?);" # all columns + PK
            param_tuple = (
                None, # room_id is set to None for database to autoincrement
                data['room_price'], 
                data['room_num'],
                data['room_type_id']
            )    
            cur.execute(query, param_tuple)
            result['message'] = 'room added successfully!' 

            # OPTIONAL: Get the id of record inserted - cursor should be still open
            # Might be useful later in more advanced cases
            # e.g. when inserting records in 2 tables at the same time for 1:m transactions
            inserted_room_id = cur.lastrowid
            print(f"inserted_room_id: {inserted_room_id}")
            result['room_id'] = inserted_room_id

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            # This part of the code is executed if an error occured when executing any statement in the try block
            result['message'] = 'Create room failed!' 
            print(f"Database {DATABASE_URI} - Create room failed!")
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

    def find_by_id(self, room_id):
        """
        Find a record by id

        Parameters: room id 

        Return: data search result
        """
        
        # Print info for debugging
        print("\nFinding a room ...\n")
        print(f"room_id: {room_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.row_factory = sqlite3.Row # to be able to use row.keys()
            cur = conn.cursor()
            query = "SELECT * FROM room WHERE room_id=?;"
            param_tuple = (room_id, ) # Works as this is a tuple of length 1
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
                result['room'] = d
            else:    
                result['message'] = "room not found!"
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

    def find_by_room_tlt(self, room_type_id):
        """
        Filter room records by room title (eg. delux, family...)

        Parameters: room title

        Return: data search result
        """
        # Print info for debugging
        print("\nFinding room(s) by room_type_id ...\n")
        if room_type_id:
            print(f"room_type_id: {room_type_id}")
        else:
            print("no text input")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # query = "SELECT * FROM room WHERE room_type_id LIKE ?;" # Partial match
            query = "SELECT * FROM room WHERE room_type_id = ?;" # Exact match
            param_tuple = (room_type_id, ) # If a single value, must have a comma at the end!
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
                result['filtered_room_tlts_ids'] = list_staffs_id

            else:    
                result['message'] = "No staffs found!"
                result['bookings'] = []
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Find by room_tlt failed!' 
            print(f"Database {DATABASE_URI} - Find by room_tlt failed!")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")   
        return result  # return the result as a dictionary   

    def find_all(self):
        """
        Find all room records

        Parameters: None

        Return: data search result
        """
        # Print info for debugging
        print("\nFinding all rooms ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM room;"
            #param_tuple = ()
            #cur.execute(query, param_tuple)
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one rooms - so create a list
                list_rooms = [] # Create an empty list to append rooms dicts
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

                    list_rooms.append(d) # Append the room dict to the room list
                    pass     

                # After the for loop
                # Store room list in result dict under key "rooms" - PLURAL             
                result['rooms'] = list_rooms    
            else:    
                result['message'] = "No room found!"
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
        This is a special method similar to find_all but returns room_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all rooms ids ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT room_id FROM room;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                result['room_ids'] = [x[0] for x in rows] # List comprehension to grab first element of the tuple
            else:    
                result['message'] = "No rooms found!"
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

    def update(self, room_id, data):
        """
        Updating one record from a table

        Parameters: room id to be changed

        Return: data insertion result
        """

        # Print info for debugging
        print("\nUpdating room ...\n")
        print(f"room_id: {room_id}")
        print(f"data: {data}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # Update all the attributes in room table except room_id
            query = """UPDATE room
               SET 
                  room_price=?, 
                  room_num=?,
                  room_type_id=?
              WHERE 
                  room_id = ?;"""
            param_tuple = (
                data['room_price'], 
                data['room_num'], 
                data['room_type_id'],
                room_id)
            cur.execute(query, param_tuple)
            result['message'] = 'room Updated!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'room NOT updated!' 
            print(f"Database {DATABASE_URI} - Update room failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result

    def delete(self, room_id):
        """
        Deleting one record from a table

        Parameters: room id to be deleted

        Return: data deletion result
        """

        # Print info for debugging
        print("\nDeleting room ...\n")
        print(f"room_id: {room_id}")
 
        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.execute("PRAGMA foreign_keys = 1")
            cur = conn.cursor()
            query = "DELETE FROM room WHERE room_id = ?;"
            param_tuple = (room_id, )
            cur.execute(query, param_tuple)
            result['message'] = 'room deleted!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'room NOT deleted!' 
            print(f"Database {DATABASE_URI} - Delete room failed")
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
            # Create the room table
            cur.execute(DATA_RETRIEVE_SQL)
            fetched_df = cur.fetchall()
            return fetched_df
