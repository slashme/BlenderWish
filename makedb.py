import sqlite3
con = sqlite3.connect('wishes.db')
con.execute('''
CREATE TABLE projectstatus (
  statusid INTEGER PRIMARY KEY,
  name TEXT NOT NULL
  )
''')
con.execute('''
CREATE TABLE clientstatus (
  statusid INTEGER PRIMARY KEY,
  name TEXT NOT NULL
  )
''')
con.execute('''
CREATE TABLE framestatus (
  statusid INTEGER PRIMARY KEY,
  name TEXT NOT NULL
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
  ext TEXT NOT NULL,
  name TEXT NOT NULL)
''')
con.execute('''
CREATE TABLE frames (
  frameid INTEGER PRIMARY KEY,
  status INTEGER NOT NULL,
  wishid INTEGER NOT NULL,
  framenumber INTEGER,
  clientid INTEGER,
  draftfilename TEXT,
  filename TEXT,
  renderstart TEXT,
  renderend TEXT,
  uploadstart TEXT,
  uploadend TEXT,
  FOREIGN KEY(status) REFERENCES framestatus(statusid),
  FOREIGN KEY(wishid) REFERENCES wishes(wishid),
  FOREIGN KEY(clientid) REFERENCES clients(clientid))
''')
con.execute('''
CREATE TABLE engines (
  engineid INTEGER PRIMARY KEY,
  name TEXT NOT NULL)
''')
con.execute('''
CREATE TABLE wishes (
  wishid INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  majorversion INTEGER NOT NULL,
  minorversion INTEGER NOT NULL,
  versionsuffix TEXT,
  status INTEGER NOT NULL,
  frametype INTEGER NOT NULL,
  firstframe INTEGER,
  lastframe INTEGER,
  engine INTEGER NOT NULL,
  FOREIGN KEY(status) REFERENCES projectstatus(statusid),
  FOREIGN KEY(frametype) REFERENCES frametypes(frametypeid),
  FOREIGN KEY(engine) REFERENCES engines(engineid))
''')
#Populate engines table
con.execute("INSERT INTO engines (name) VALUES ('internal')")
con.execute("INSERT INTO engines (name) VALUES ('cycles')")
#Populate client status table
con.execute("INSERT INTO clientstatus (name) VALUES ('new')")
con.execute("INSERT INTO clientstatus (name) VALUES ('good')")
con.execute("INSERT INTO clientstatus (name) VALUES ('bad')")
#Populate frame status table
con.execute("INSERT INTO framestatus (name) VALUES ('empty')")
con.execute("INSERT INTO framestatus (name) VALUES ('draft')")
con.execute("INSERT INTO framestatus (name) VALUES ('running')")
con.execute("INSERT INTO framestatus (name) VALUES ('done')")
#Populate project status table
con.execute("INSERT INTO projectstatus (name) VALUES ('stopped')")
con.execute("INSERT INTO projectstatus (name) VALUES ('running')")
con.execute("INSERT INTO projectstatus (name) VALUES ('complete')")
#Populate frametypes table - just some basic values; fix later.
con.execute("INSERT INTO frametypes (ext, name) VALUES ('png','Portable Network Graphics')")
con.execute("INSERT INTO frametypes (ext, name) VALUES ('jpg','JPEG')")
con.execute("INSERT INTO frametypes (ext, name) VALUES ('exr','OpenEXR')")
con.commit()
