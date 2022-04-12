# delete_person_parameterised.py

# Libraries
import sqlite3

# 1. Open a connection
with sqlite3.connect("example.db") as conn:
    # 2. Get a cursor from the connection
    cur = conn.cursor()
    # 3. Build a query using parameterized SQL statements
    query = "DELETE FROM person WHERE person_id = ?;"
    param_tuple = (1,) # note: must have a comma after 1 otherwise python won't know it's a tuple
    # 4. Use the cursor to execute the SQL
    cur.execute(query, param_tuple)



    