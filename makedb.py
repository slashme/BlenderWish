import sqlite3
con = sqlite3.connect('wishes.db')
con.execute('''
CREATE TABLE status (
  statusid INTEGER PRIMARY KEY,
  name char(20) NOT NULL
  )
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
  FOREIGN KEY(status) REFERENCES status(statusid),
  FOREIGN KEY(frametype) REFERENCES frametypes(frametypeid),
  FOREIGN KEY(engine) REFERENCES engines(engineid))
''')
#Populate engines table
con.execute("INSERT INTO engines (name) VALUES ('Internal')")
con.execute("INSERT INTO engines (name) VALUES ('cycles')")
#Populate status table
con.execute("INSERT INTO status (name) VALUES ('stopped')")
con.execute("INSERT INTO status (name) VALUES ('running')")
con.execute("INSERT INTO status (name) VALUES ('complete')")
#Populate frametypes table - just some basic values; fix later.
con.execute("INSERT INTO frametypes (ext, name) VALUES ('png','Portable Network Graphics')")
con.execute("INSERT INTO frametypes (ext, name) VALUES ('jpg','JPEG')")
con.execute("INSERT INTO frametypes (ext, name) VALUES ('exr','OpenEXR')")
con.commit()
