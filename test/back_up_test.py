import sqlite3

con = sqlite3.connect('../sqlite3.db')
cur = con.cursor()


with open('./db1_dump.sql','w') as f :
    for line in con.iterdump():
        f.write('%s\n' %line)