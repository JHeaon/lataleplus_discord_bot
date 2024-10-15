import sqlite3
import os

def init():
    os.system("touch ../sqlite3.db")
    con = sqlite3.connect('../sqlite3.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE Announcement("
                "id INTEGER PRIMARY KEY,"
                "title text,"
                "contents text,"
                "url text"");")

    cur.execute("CREATE TABLE InspectionUpdate("
                "id INTEGER PRIMARY KEY,"
                "title text,"
                "contents text,"
                "url text"");")

    cur.execute("CREATE TABLE DeveloperNote("
                "id INTEGER PRIMARY KEY,"
                "title text,"
                "contents text,"
                "url text"");")

    cur.execute("CREATE TABLE Event("
                "id INTEGER PRIMARY KEY,"
                "title text,"
                "contents text,"
                "url text"");")

    cur.execute("CREATE TABLE EventWinner("
                "id INTEGER PRIMARY KEY,"
                "title text,"
                "contents text,"
                "url text"");")

    cur.execute("CREATE TABLE FreeBulletInBoard("
                "id INTEGER PRIMARY KEY,"
                "title text,"
                "contents text,"
                "url text"");")

    con.commit()
    con.close()


init()
