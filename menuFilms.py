import sqlite3
import readFilms, addFilms, updateFilmV2, deleteFilms, reportsFilm

# function to read the contents in the menuoptionsFilms.txt file
def read_menu():
    with open("menuoptionsFilms.txt") as fileRead:
        UserMenu = fileRead.read()
    return UserMenu

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

# Main program
mainProgram = True

while mainProgram:
    print("\nThe Films Menu options.")
    print("Enter:")
    print("1. Print all Films.")
    print("2. Add a film.")
    print("3. Update a film.")
    print("4. Delete a film.")
    print("5. Report.")
    print("6. Exit the Films App.")

    menu = input("Enter an option from the films menu: ")

    if menu == "1":
        readFilms.read_film()
    elif menu == "2":
        addFilms.insert_film()
    elif menu == "3":
        update_films()
    elif menu == "4":
        deleteFilms.delete_films()
    elif menu == "5":
        reportsFilm.reports_film()
    else:
        mainProgram = False

input("Press Enter to quit the Films App")
