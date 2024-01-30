from connectFilms import *



# create a subroutine
def delete_films():
    filmidfield = input("Enter filmID for the record to be deleted:")

    # delete the record with the film id entered
    dbCursor.execute(f"DELETE FROM tblfilms WHERE filmID = ?", (filmidfield,))
    dbCon.commit()

    print(f"Record {filmidfield} deleted from the tblfilms")

if __name__ == "__main__":
    delete_films()


