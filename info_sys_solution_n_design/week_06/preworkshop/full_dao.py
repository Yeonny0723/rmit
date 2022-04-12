# person_dao.py
 
# Import packages
import sqlite3

# Constants
DATABASE_URI = 'example.db'

class PersonDAO():

    def create(self, data):

        # Print info for debugging
        print("\nCreating a person ...\n") #\n means print("\n") a blank line
        print(f"data: {data}")

        result = {}

        # Parameterized Query i.e. question marks as placeholders for  actual values
        conn = None # First initialise the connection to None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "INSERT INTO person VALUES (?, ?, ?);" # all columns + PK
            param_tuple = (
                None, # person_id is set to None for database to autoincrement
                data['firstname'], 
                data['lastname']
            )    
            cur.execute(query, param_tuple)
            result['message'] = 'Person added successfully!' 

            # OPTIONAL: Get the id of record inserted - cursor should be still open
            # Might be useful later in more advanced cases
            # e.g. when inserting records in 2 tables at the same time for 1:m transactions
            inserted_person_id = cur.lastrowid
            print(f"inserted_person_id: {inserted_person_id}")
            result['person_id'] = inserted_person_id

            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            # This part of the code is executed if an error occured when executing any statement in the try block
            result['message'] = 'Create person failed!' 
            print(f"Database {DATABASE_URI} - Create person failed!")
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

    def find_by_id(self, person_id):

        # Print info for debugging
        print("\nFinding a person ...\n")
        print(f"person_id: {person_id}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            conn.row_factory = sqlite3.Row # to be able to use row.keys()
            cur = conn.cursor()
            query = "SELECT * FROM person WHERE person_id=?;"
            param_tuple = (person_id, ) # Works as this is a tuple of length 1
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
                result['person'] = d
            else:    
                result['message'] = "Person not found!"
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

        # Print info for debugging
        print("\nFinding person(s) by lastname ...\n")
        print(f"lastname: {lastname}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            #query = "SELECT * FROM person WHERE lastname LIKE ?;" # Partial match
            query = "SELECT * FROM person WHERE lastname = ?;" # Exact match
            param_tuple = (lastname, ) # If a single value, must have a comma at the end!
            cur.execute(query, param_tuple)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one persons - so create a list
                list_persons = [] # Create an empty list to append person dicts
                for x in rows: # rows is a list of SQlite objects - process one by one
                    # cursor.description contains the name of the columns
                    # Use dictionary compejension to build the dictionary
                    # Use list comprehension - get olumn names from cursor.description
                    # The column name is at index 0 i.e. the first position
                    col_names = [description[0] for description in cur.description]
                    #print(f"Column names: {col_names}")
                    # Using dictionary comprehension and enumerate() 
                    #  to match the column names with their index positions
                    d = {key: x[i] for i, key in enumerate(col_names)} # works

                    list_persons.append(d) # Append the person dict to the person list
                      
                # Store the person list in the result dict under key "persons"              
                result['persons'] = list_persons                

            else:    
                result['message'] = "No persons found!"
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

        # Print info for debugging
        print("\nFinding all persons ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT * FROM person;"
            #param_tuple = ()
            #cur.execute(query, param_tuple)
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                print(f"rows: {rows}")

                # Convert the list of row objects to a list of dictionaries
                # This query could return more than one persons - so create a list
                list_persons = [] # Create an empty list to append person dicts
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

                    list_persons.append(d) # Append the person dict to the person list
                    pass     

                # After the for loop
                # Store person list in result dict under key "persons" - PLURAL             
                result['persons'] = list_persons    
            else:    
                result['message'] = "No persons found!"
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
        This is a special method similar to find_all but returns person_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all person ids ...\n")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "SELECT person_id FROM person;"
            cur.execute(query)
            rows = cur.fetchall()
            if rows:
                result['person_ids'] = [x[0] for x in rows] # List comprehension to grab first element of the tuple
            else:    
                result['message'] = "No persons found!"
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

    def update(self, person_id, data):

        # Print info for debugging
        print("\nUpdating person ...\n")
        print(f"person_id: {person_id}")
        print(f"data: {data}")

        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            # Update all the attributes in person table except person_id
            query = """UPDATE person
               SET 
                  firstname=?, 
                  lastname=?
              WHERE 
                  person_id = ?;"""
            param_tuple = (
                data['firstname'], 
                data['lastname'], 
                person_id)
            cur.execute(query, param_tuple)
            result['message'] = 'Person Updated!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Person NOT updated!' 
            print(f"Database {DATABASE_URI} - Update person failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result

    def delete(self, person_id):

        # Print info for debugging
        print("\nDeleting person ...\n")
        print(f"person_id: {person_id}")
 
        # Create a blank dictionary to return the result
        result = {}

        # Using Parameterised Query
        conn = None
        try:
            conn = sqlite3.connect(DATABASE_URI)
            cur = conn.cursor()
            query = "DELETE FROM person WHERE person_id = ?;"
            param_tuple = (person_id, )
            cur.execute(query, param_tuple)
            result['message'] = 'Person deleted!' 
            cur.close()
            conn.commit()
        except sqlite3.Error as error:
            result['message'] = 'Person NOT deleted!' 
            print(f"Database {DATABASE_URI} - Delete person failed")
            print(error)
        finally:
            if conn:
                conn.close()
                #print("Database closed")

        #print(f"result: {result}")
        return result # return the result as a dictionary    


# Dao implementation

# 1. Instantiate the person DAO
person_dao = PersonDAO()

# 2. Set up the data to insert
data = {
    'firstname':"Hamish",
    'lastname': "Pollard"
}

# 3. Call the create() method on the DAO
# Pass the data as param
# And store the returned value somewhere
result = person_dao.create(data)