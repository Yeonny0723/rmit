# read_person.py

# Libraries
import sqlite3

# 1. Open a connection
with sqlite3.connect("example.db") as conn:
    # 2. Get a cursor from the connection
    cur = conn.cursor()
    # 3. Use the cursor to execute the SQL
    # cur.execute("SELECT * FROM person WHERE person_id = 1;") 
    # # Use single double quotes for strings on one line
    cur.execute("SELECT * FROM person;") # Use single double quotes for strings on one line
    # 4. Get the results 
    row = cur.fetchone() # fetchone will return the first row
    # running fetchone() again will return you the second row
    print(row)

