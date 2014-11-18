import sqlite3
import sys

conn = sqlite3.connect("fileTimeCapsule.db")
conn.row_factory = sqlite3.Row

#wrapper for functions that need a database cursor.
def DBwrapper(func):
    def cleanup(*args, **kwargs):
        c = conn.cursor()
        r = func(c, *args, **kwargs)
        c.close()
        conn.commit()
        return r
    return cleanup

#Stores file details in sqlite and file in filesystem
#All one transaction if either part fails, all fails
@DBwrapper
def newFile(c, uploadedFile, date, notes):
    #store file details
    c.execute("""INSERT INTO file (name, comment, date_accessible, user)
                 VALUES (?, ?, ?, 1)""", (uploadedFile["filename"], notes, int(date)))
    ID = str(c.lastrowid)

    #store file
    with open("fileDB/" + ID, "wb") as newFile:
        fileData = uploadedFile["body"]
        #ensure file < 10 MB
        if sys.getsizeof(fileData) / (1024 ** 2) > 10:
            raise IOError
        newFile.write(fileData)
    return ID

@DBwrapper
def getFile(c, ID):
    c.execute("SELECT name, comment, date_accessible, user FROM file WHERE file_ID = ?", (ID,))
    return c.fetchone()

#closes all DB connections
def cleanup():
    conn.close()
