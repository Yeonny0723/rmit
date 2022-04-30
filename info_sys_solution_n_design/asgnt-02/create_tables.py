# create_tables.py

# ###########
# 1. Libraries
# ###########
import sqlite3


# ###########
# 2. Constants
# ###########
DATABASE_URI = "ahs_reservation.db"


# For AUTOINCREMENTED PK (whether implied or not)

CUSTOMER_SQL = """
    CREATE TABLE customer (
        customer_id           INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name            VARCHAR(50) NOT NULL,
        lastname              VARCHAR(50) NOT NULL,
        phone_num             VARCHAR(50) NOT NULL UNIQUE, 
        email                 VARCHAR(50) NOT NULL UNIQUE,
        credit_card_num       VARCHAR(50) NOT NULL,
        expiry_date           VARCHAR(50) NOT NULL,
        cvc_code              VARCHAR(50) NOT NULL,
        dob                   VARCHAR(50) NOT NULL
)
"""

STAFF_SQL = """
    CREATE TABLE staff (
        staff_id                INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name              VARCHAR(50) NOT NULL,
        lastname                VARCHAR(50) NOT NULL,
        email                   VARCHAR(50) NOT NULL UNIQUE,
        title                   VARCHAR(50) NOT NULL
)
"""

ROOM_TYPE_SQL = """
    CREATE TABLE room_type (
        room_type_id                 INTEGER PRIMARY KEY AUTOINCREMENT,
        room_type_tlt                VARCHAR(50) NOT NULL,
        king_bed_count               INTEGER NOT NULL,
        queen_bed_count              INTEGER NOT NULL,
        single_bed_count             INTEGER NOT NULL,
        bath_room_count              INTEGER NOT NULL
)
"""

ROOM_SQL = """
    CREATE TABLE room (
        room_id                     INTEGER PRIMARY KEY AUTOINCREMENT,
        room_price                  DOUBLE NOT NULL,
        room_num                    INTEGER NOT NULL,
        room_type_id                INTEGER NOT NULL,
        FOREIGN KEY(room_type_id)   REFERENCES room_type(room_type_id) ON DELETE CASCADE
)
"""

BOOKING_SQL = """
    CREATE TABLE booking (
        booking_id                INTEGER PRIMARY KEY AUTOINCREMENT,
        check_in                  TEXT,
        check_out                 TEXT,
        extra_bed                 BOOLEAN NOT NULL,
        adult_num                 INTEGER NOT NULL,
        child_num                 INTEGER NOT NULL,
        infant_num                INTEGER NOT NULL,
        total_price               DOUBLE NOT NULL,
        booking_dtm               TEXT,
        room_id                   INTEGER NOT NULL,
        staff_id                  INTEGER NOT NULL,
        customer_id               INTEGER NOT NULL,
        phone_num                 VARCHAR(50) NOT NULL,
        FOREIGN KEY(room_id)      REFERENCES room(room_id) ON DELETE CASCADE
        FOREIGN KEY(staff_id)     REFERENCES staff(staff_id) ON DELETE CASCADE
        FOREIGN KEY(customer_id)  REFERENCES customer(customer_id) ON DELETE CASCADE
)
"""



"""
Please note that SQLite does not enforce foreign key constraints by default
To enable it, need to execute the following command after you connect to the database
    PRAGMA foreign_keys = 1

e.g.
conn=sqlite3.connect("yourdatabase.db")
conn.execute("PRAGMA foreign_keys = 1")
cur=conn.cursor()

"""

# ###########
# 3. Functions
# ###########


# ###########
# 4. Main method
# ###########

if __name__ == '__main__':

    print("Creating the database and tables") 
    print("Please ensure that you've deleted ahs_reservation.db in the currect folder")

    print()
    input("Press Enter to continue or Ctrl+C to cancel ...")

    # Open a connection
    conn = sqlite3.connect(DATABASE_URI)
    print(f"Opened a connection to database {DATABASE_URI}")

    with conn:
        # Get a cursor
        cur = conn.cursor()
        print("Got a cursor to the connection")

        # Create the customer table
        cur.execute(CUSTOMER_SQL)
        print(f"Customer table created in database {DATABASE_URI}")
        # Create the staff table
        cur.execute(STAFF_SQL)
        print(f"Staff table created in database {DATABASE_URI}")
        # Create the room type table
        cur.execute(ROOM_TYPE_SQL)
        print(f"Room type table created in database {DATABASE_URI}")
        # Create the room table
        cur.execute(ROOM_SQL)
        print(f"Room table created in database {DATABASE_URI}")
        # Create the booking table
        cur.execute(BOOKING_SQL)
        print(f"Booking table created in database {DATABASE_URI}")

    print("\nAll done!")                    

    print("\nPlease use DB Browser for SQLite to check the database!")  