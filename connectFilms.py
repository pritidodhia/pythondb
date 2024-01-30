# import sqlite3 as sql # import the sqlite module and assign it an Alias 'sql'

# # To use the sqlite module 
# "Create a variable called dbCon"
# dbCon = sql.connect("filmflixnew.db")

# # create cursor object using the cursor method to run sql queries
# "dbCursor is a variable"
# dbCursor = dbCon.cursor() # cursor() is a method



import sqlite3 as sql

dbCon = sql.connect("filmflixnew.db")
dbCursor = dbCon.cursor()

dbCursor.execute('''
    CREATE TABLE IF NOT EXISTS tblfilms (
        filmID INTEGER PRIMARY KEY,
        title TEXT,
        yearReleased INTEGER,
        rating TEXT,
        duration INTEGER,
        genre TEXT
    )
''')

dbCon.commit()
