

from connectFilms import *

# create a subroutine 
def insert_film():
    # FilmID field is auto increment (no data input is required)

    # ask for user input for Title, yearReleased, rating, duration, and genre
    filmID = input("Enter film ID: ")
    filmTitle = input("Enter film Title: ")
    yearReleased = int(input("Enter year Released: ")) 
    rating = input("Enter rating: ")
    duration = int(input("Enter duration: "))
    genre = input("Enter genre: ")

    # data from Title, YearReleased, Rating, Duration, and Genre variables and save it into the database.
    dbCursor.execute("INSERT INTO tblfilms (filmID,title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?, ?)",
                    (filmID,filmTitle, yearReleased, rating, duration, genre))
    
    # Permanently save the record in the tblfilms table in the database
    dbCon.commit()

    print(f"{filmTitle} inserted in the tblFilms.")

if __name__ == "__main__":
    insert_film()

