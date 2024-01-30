import sqlite3
import os

# Function to connect to the SQLite database
def connect_to_database():
    connection = sqlite3.connect("filmflixnew.db")
    cursor = connection.cursor()
    return connection, cursor

# Function to close the database connection
def close_connection(connection):
    connection.close()

# Function to update a record in tblFilms
def update_films():
    filmidfield = input("Enter FilmID for the record to be updated:")
    
    # Get the list of field names
    fields = input("Enter the field name to be updated (e.g., title, yearReleased, rating, duration, genre):").split(',')

    # Initialize the update query
    update_query = f"UPDATE tblFilms SET {', '.join(f.strip() + '=?' for f in fields)} WHERE filmID=?"

    # Loop through the fields
    field_values = [input(f"Enter the new value for the field {field.strip()}:") for field in fields]

    # Connect to the database
    dbCon, dbCursor = connect_to_database()

    # Execute the query
    dbCursor.execute(update_query, (*field_values, filmidfield))
    dbCon.commit()

    print("Record updated successfully!")

    # Close the connection
    close_connection(dbCon)

# Run the update_films function
update_films()
