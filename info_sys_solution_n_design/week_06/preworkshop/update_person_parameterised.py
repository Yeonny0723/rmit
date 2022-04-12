# update_person_parameterised.py

# Libraries
import sqlite3

# 1. Open a connection
with sqlite3.connect("example.db") as conn:
    # 2. Get a cursor from the connection
    cur = conn.cursor()
    # 3. Build a query using parameterized SQL statements
    query = """UPDATE person 
        SET firstname=?, 
            lastname=? 
        WHERE person_id = ?;"""
    param_tuple = (
        "Cheun",
        "Jo",
        2) # note: no need for a comma at the end as Python knows it's a tuple
    # 4. Use the cursor to execute the SQL
    cur.execute(query, param_tuple)


    