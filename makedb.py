import sqlite3
con = sqlite3.connect('wishes.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE status (statusid INTEGER PRIMARY KEY, name char(20) NOT NULL)")
con.execute("INSERT INTO status (statusid, name) VALUES (0,'stopped')")
con.execute("INSERT INTO status (statusid, name) VALUES (1,'running')")
con.execute("INSERT INTO status (statusid, name) VALUES (2,'complete')")
con.execute("CREATE TABLE wishes (wishid INTEGER PRIMARY KEY, name char(100) NOT NULL, status INTEGER NOT NULL, FOREIGN KEY(status) REFERENCES status(statusid))")
con.execute("INSERT INTO wishes (name, status) VALUES ('awish',0)")
con.commit()
