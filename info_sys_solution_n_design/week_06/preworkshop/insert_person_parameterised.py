# Libraries
import sqlite3

# 1. Open a connection
with sqlite3.connect("example.db") as conn:
    # 2. Get a cursor from the connection
    cur = conn.cursor()
    # 3. Build a query using parameterized SQL statements
    query = "INSERT INTO person VALUES (?, ?, ?);" # all 3 columns including the primary key
    param_tuple = (
        None,    # person_id - must specify "None" for the database to generate the key
        "Joe",   # firstname
        "Dalton" # lastname - note no comma after last item
    )
    # Note: the values in the tuple MUST follow the order the columns are defined in the table
    # 4. Use the cursor to execute the SQL
    cur.execute(query, param_tuple)
    # Note: when the with statement ends, cur and conn are closed automatically


    