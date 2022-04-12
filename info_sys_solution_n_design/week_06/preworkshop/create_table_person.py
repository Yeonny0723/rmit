import sqlite3 # python sql library


with sqlite3.connect("example.db") as conn: # open a connection with database
    cur = conn.cursor() # get a cursor(interface(?)) from connection
    # user a cursor to execute the code
    cur.execute("""CREATE TABLE person
        ( 
            person_id  INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname  VARCHAR(50),
            lastname   VARCHAR(50) NOT NULL
        );""")

