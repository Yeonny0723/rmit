# Libraries
import sqlite3

# 1. Open a connection
with sqlite3.connect("example.db") as conn:
    # 2. Get a cursor from the connection
    cur = conn.cursor()
    # 3. Build a query using parameterized SQL statements
    query = "SELECT * FROM person WHERE person_id = ?;"
    param_tuple = (1,) # note: must have a comma after 1 otherwise it's not a tuple
    # 4. Use the cursor to execute the SQL
    cur.execute(query, param_tuple)
    # 5. Get the results 
    row = cur.fetchone()
    print(row)

    