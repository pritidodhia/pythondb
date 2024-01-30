import sqlite3

# Function to connect to the SQLite database
def connect_to_database():
    connection = sqlite3.connect("filmflixnew.db")
    cursor = connection.cursor()
    return connection, cursor

# create subroutine
def update_films():
    # Connect to the database
    dbCon, dbCursor = connect_to_database()

    # ask for the FilmID
    filmidfield = input("Enter FilmID for the record to be updated:")

    # ask for the field/column to be updated
    fieldName = input(
        "Enter filmID, filmTitle, yearReleased, rating, duration or genre as field names: "
    ).title()

    # ask for the field/column value(new value)
    fieldValue = input(f"Enter the value for the field {fieldName} field")

    # add single quotes to the new value
    fieldValue = "'" + fieldValue + "'"

    try:
        # update a specific field for a particular record
        dbCursor.execute(f"UPDATE films SET {fieldName} = {fieldValue} WHERE FilmID = {filmidfield}")
        dbCon.commit()
        print(f"Record {filmidfield} updated in the films table")
    except Exception as e:
        print(f"Error updating record: {e}")
    finally:
        # Close the database connection
        dbCon.close()

if __name__ == "__main__":
    update_films()
