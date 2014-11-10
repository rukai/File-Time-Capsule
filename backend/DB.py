import sqlite3

conn = sqlite3.connect("fileAway.db")

def DBwrapper(func):
    def cleanup(*args, **kwargs):
        c = conn.cursor()
        func(c, *args, **kwargs)
        c.close()
        conn.commit()
    return cleanup

@DBwrapper
def newFile(c, uploadedFile, date, notes):
    c.execute("""INSERT INTO file (name, comment, date_accessible, user)
                 VALUES (?, ?, ?, 1)""", [uploadedFile["filename"], notes, date])
    # IF SQL FAIL, RETURN
    with open("fileDB/" + uploadedFile["filename"], "wb") as newFile:
        newFile.write(uploadedFile["body"])

@DBwrapper
def getFile(ID):
    return "FOOBAR_GOOBAR"


#closes all DB connections
def cleanup():
    conn.close()
