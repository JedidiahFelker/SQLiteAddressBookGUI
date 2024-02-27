"""
    Name: db_operations.py
    Author: Jed Felker
    Created: 2/4/23
    Purpose: SQLite database query execution
    controller
"""
# Import SQLite library to work with databases
import sqlite3


class DBOperations:
    def __init__(self, database: str):
        self.database = database
        self.debugging = False

# --------------------------- CREATE TABLE ----------------------------------#
    def create_table(self):
        """Create database and table if not exists"""
        # Drop table if needed to change table structure
        SQL = "DROP TABLE IF EXISTS tbl_address_book"
        self.execute_sql(SQL)
        # Create the address_book table if it doesn't exist
        SQL = """
            CREATE TABLE IF NOT EXISTS tbl_address_book(
            id          INTEGER PRIMARY KEY,
            first_name  TEXT,
            last_name   TEXT,
            phone       TEXT,
            email       TEXT
        )"""
        self.execute_sql(SQL)

# -------------------------- INSERT RECORD ----------------------------------#
    def insert_record(
        self,
        first_name: str,
        last_name: str,
        phone: str,
        email: str
    ):
        """Insert new record"""
        SQL = """
            INSERT INTO tbl_address_book
            VALUES(NULL, ?, ?, ?, ?)
        """
        # Parameters are a tuple of variables or values
        # They are mapped to the ? ? placeholders of the query
        parameters = (
            first_name,
            last_name,
            phone,
            email
        )
        self.execute_sql(SQL, parameters)

# -------------------------- FETCH ALL RECORDS ------------------------------#
    def fetch_all_records(self):
        """Fetch all records"""
        # Query to get all contacts
        # SELECT * FROM selects all records from a table
        # sorted by last name
        # desc (decsending) order for GUI Treeview
        # asc (ascending) order for CLI
        SQL = """
            SELECT * FROM tbl_address_book
            ORDER BY last_name asc
        """
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            # fetchall() fetches the records returned by the SQL
            # statement as a list of tuples
            records = cursor.execute(SQL).fetchall()
        if records:
            return records
        
# -------------------------- UPDATE RECORD ----------------------------------#
    def update_record(
        self,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        id: int
    ):
        """Update selected record by id"""
        SQL = """
            UPDATE tbl_address_book
            SET first_name = ?,
            last_name = ?,
            phone = ?,
            email = ?,
            WHERE id = ?
        """
        # Parameters are a tuple of variables or values
        # They are mapped to the ? ? ? ? ? in the query
        parameters = (
            first_name,
            last_name,
            phone,
            email,
            id
        )
        self.execute_sql(SQL, parameters)

# -------------------------- DELETE RECORD ----------------------------------#
    def delete_record(self, id: int):
        """Deleter selected record by id"""
        SQL = """
            DELETE FROM tbl_address_book
            WHERE id = ?
        """
        # Parameters are a tuple of variables or values
        # They are mapped to the ? in the query
        parameters = (
            id,
        )
        self.execute_sql(SQL, parameters)

# -------------------------- DATABASE DUMP TO SQL FILE ----------------------#
    def database_dump(self):
        try:
            with sqlite3.connect(self.database) as connection:
                # Iterate through database, print SQL
                for line in connection.iterdump():
                    print(line)
                
                # Use with context manager to write and close/save the file
                with open("database_dump.sql", "w") as file:
                    # Iterate through database, write SQL to file
                    for line in connection.iterdump():
                        file.write(f"{line}\n")
                print("File written to disk.")
        except Exception as e:
            print(f"There was an SQLite error: {e}")

# -------------------------- EXECUTE SQL ------------------------------------#
    def execute_sql(self, SQL: str, parameters: tuple = None):
        # This is an overloaded method in Python, parameters is optional
        # If everything inside the with sqlite3.connect is successful
        # connect.commit() and connect.close() are automatically called
        # when the with statement exits
        # If DATABASE does not exist, it is created
        try:
            with sqlite3.connect(self.database) as connection:
                # Create cursor to work with SQL
                cursor = connection.cursor()
                if parameters is not None:
                    # Execute SQL with parameters
                    cursor.execute(SQL, parameters)
                else:
                    # Execute SQL without parameters
                    cursor.executescript(SQL)
                # Records are written automatically
                # after the with statement exits
                # All connections are closed
        except Exception as e:
            print(f"There was an SQLite error: {e}")