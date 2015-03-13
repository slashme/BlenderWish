import sqlite3
con = sqlite3.connect('wishes.db')
con.execute('''
CREATE TABLE projectstatus (
  statusid INTEGER PRIMARY KEY,
  name char(20) NOT NULL
  )
''')
con.execute('''
CREATE TABLE clientstatus (
  statusid INTEGER PRIMARY KEY,
  name char(20) NOT NULL
  )
''')
con.execute('''
CREATE TABLE clients (
  clientid INTEGER PRIMARY KEY,
  ip INTEGER,
  status INTEGER NOT NULL,
  FOREIGN KEY(status) REFERENCES clientstatus(statusid))
''')
con.execute('''
CREATE TABLE frametypes (
  frametypeid INTEGER PRIMARY KEY,
  ext char(10) NOT NULL,
  name char(50) NOT NULL)
''')
con.execute('''
CREATE TABLE engines (
  engineid INTEGER PRIMARY KEY,
  name char(20) NOT NULL)
''')
con.execute('''
CREATE TABLE wishes (
  wishid INTEGER PRIMARY KEY,
  name char(100) NOT NULL,
  majorversion INTEGER NOT NULL,
  minorversion INTEGER NOT NULL,
  versionsuffix char(10),
  status INTEGER NOT NULL,
  frametype INTEGER NOT NULL,
  engine INTEGER NOT NULL,
  FOREIGN KEY(status) REFERENCES projectstatus(statusid),
  FOREIGN KEY(frametype) REFERENCES frametypes(frametypeid),
  FOREIGN KEY(engine) REFERENCES engines(engineid))
''')
#Populate engines table
con.execute("INSERT INTO engines (name) VALUES ('Internal')")
con.execute("INSERT INTO engines (name) VALUES ('cycles')")
#Populate client status table
con.execute("INSERT INTO clientstatus (name) VALUES ('new')")
con.execute("INSERT INTO clientstatus (name) VALUES ('good')")
con.execute("INSERT INTO clientstatus (name) VALUES ('bad')")
#Populate project status table
con.execute("INSERT INTO projectstatus (name) VALUES ('stopped')")
con.execute("INSERT INTO projectstatus (name) VALUES ('running')")
con.execute("INSERT INTO projectstatus (name) VALUES ('complete')")
#Populate frametypes table - just some basic values; fix later.
con.execute("INSERT INTO frametypes (ext, name) VALUES ('png','Portable Network Graphics')")
con.execute("INSERT INTO frametypes (ext, name) VALUES ('jpg','JPEG')")
con.execute("INSERT INTO frametypes (ext, name) VALUES ('exr','OpenEXR')")
con.commit()
