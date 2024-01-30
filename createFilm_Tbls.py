# from connectFilms import * 


# dbCursor.execute
# ('''
#     CREATE TABLE IF NOT EXISTS films (
#         filmID INTEGER PRIMARY KEY,
#         title TEXT,
#         yearReleased INTEGER,
#         rating TEXT,
#         duration INTEGER,
#         genre TEXT
#     )
# ''')
import sqlite3

# Function to connect to the SQLite database
def connect_to_database():
    connection = sqlite3.connect("filmflixnew.db")
    cursor = connection.cursor()
    return connection, cursor

# Create the films table if it doesn't exist
def create_films_table():
    connection = sqlite3.connect("filmflixnew.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tblfilms (
            FilmID INTEGER PRIMARY KEY,
            filmTitle TEXT,
            yearReleased INTEGER,
            rating REAL,
            duration INTEGER,
            genre TEXT
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_films_table()
