#!/usr/bin/env python3
# Copyright 2014 Lucas Kent
# Licenced under the GNU GPL V3
# Generates a fresh SQLite DB for use with File Time Capsule

import os
import sqlite3

dbfile = "fileTimeCapsule.db"

def generateDB():
    try:
        os.mkdir("fileDB")
    except FileExistsError:
        pass

    #check with user
    if(os.path.isfile(dbfile)):
        if(input("Overwrite entire SQLite DB? [y/n] ") == "y"):
            try:
                os.remove(dbfile)
            except FileNotFoundError:
                pass
        else:
            return


    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    
    #table for storing details of user uploaded files
    c.execute("""CREATE TABLE file(
                 file_ID INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 comment TEXT DEFAULT '',
                 date_created INTEGER DEFAULT (strftime('%s', 'now')),
                 date_accessible INTEGER NOT NULL,
                 user INTEGER,
                 FOREIGN KEY(user) REFERENCES user(user_ID)
                 )""")

    #table for storing users
    c.execute("""CREATE TABLE user(
                 user_ID INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 pass TEXT NOT NULL,
                 email TEXT NOT NULL,
                 date_created INTEGER DEFAULT (strftime('%s', 'now'))
                 )""")

    #dummy user
    c.execute("""INSERT INTO user (name, pass, email)
                 VALUES ('nobody', 'x', 'nobody@nowhere.org')
                 """)

    conn.commit()
    conn.close()

generateDB()
