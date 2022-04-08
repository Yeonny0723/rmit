# update_person.py

# Libraries
import sqlite3

# 1. Open a connection
with sqlite3.connect("example.db") as conn:
    # 2. Get a cursor from the connection
    cur = conn.cursor()
    # 3. Use the cursor to execute the SQL
    cur.execute("""UPDATE person 
        SET firstname='Alex', lastname='Smith' 
        WHERE person_id = 1;""")
    # Note: enclose the string values with single quotation marks
    # Otherwise will get an error like this
    # sqlite3.OperationalError: near ""UPDATE person SET firstname="": syntax error 

    