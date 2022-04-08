# delete_person.py

# Libraries
import sqlite3

# 1. Open a connection
with sqlite3.connect("example.db") as conn:
    # 2. Get a cursor from the connection
    cur = conn.cursor()
    # 3. Use the cursor to execute the SQL
    cur.execute("DELETE FROM person WHERE person_id = 1;")


    