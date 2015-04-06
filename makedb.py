import sqlite3
con = sqlite3.connect('wishes.db')
con.execute('''
CREATE TABLE projectstatus (
  status TEXT PRIMARY KEY
  )
''')
con.execute('''
CREATE TABLE clientstatus (
  status TEXT PRIMARY KEY
  )
''')
con.execute('''
CREATE TABLE framestatus (
  status TEXT PRIMARY KEY
  )
''')
con.execute('''
CREATE TABLE clients (
  clientid INTEGER PRIMARY KEY,
  ip INTEGER,
  status TEXT NOT NULL,
  FOREIGN KEY(status) REFERENCES clientstatus(status))
''')
con.execute('''
CREATE TABLE frametypes (
  frametypeid INTEGER PRIMARY KEY,
  ext TEXT NOT NULL,
  name TEXT NOT NULL)
''')
con.execute('''
CREATE TABLE blendfiles (
  blendfileid INTEGER PRIMARY KEY,
  wishid INTEGER NOT NULL,
  filename TEXT,
  uploadtime TEXT,
  FOREIGN KEY(wishid) REFERENCES wishes(wishid))
''')
con.execute('''
CREATE TABLE frames (
  frameid INTEGER PRIMARY KEY,
  status TEXT NOT NULL,
  wishid INTEGER NOT NULL,
  framenumber INTEGER,
  clientid INTEGER,
  draftfilename TEXT,
  filename TEXT,
  renderstart TEXT,
  renderend TEXT,
  uploadstart TEXT,
  uploadend TEXT,
  FOREIGN KEY(status) REFERENCES framestatus(status),
  FOREIGN KEY(wishid) REFERENCES wishes(wishid),
  FOREIGN KEY(clientid) REFERENCES clients(clientid))
''')
con.execute('''
CREATE TABLE engines (
  name TEXT PRIMARY KEY)
''')
con.execute('''
CREATE TABLE wishes (
  wishid INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  majorversion INTEGER NOT NULL,
  minorversion INTEGER NOT NULL,
  versionsuffix TEXT,
  status TEXT NOT NULL,
  frametype INTEGER NOT NULL,
  firstframe INTEGER,
  lastframe INTEGER,
  engine TEXT NOT NULL,
  FOREIGN KEY(status) REFERENCES projectstatus(status),
  FOREIGN KEY(frametype) REFERENCES frametypes(frametypeid),
  FOREIGN KEY(engine) REFERENCES engines(name))
''')
#Create table of tables
con.execute('''
CREATE TABLE alltables (
  name TEXT PRIMARY KEY
  )
''')
#Create table of user-editable fields
con.execute('''
CREATE TABLE userfields (
  id INTEGER PRIMARY KEY,
  tableid TEXT NOT NULL,
  field TEXT NOT NULL,
  editable INTEGER NOT NULL,
  FOREIGN KEY(tableid) REFERENCES alltables(name)
  )
''')
#Populate engines table
con.execute("INSERT INTO engines (name) VALUES ('cycles')")
con.execute("INSERT INTO engines (name) VALUES ('internal')")
#Populate client status table
con.execute("INSERT INTO clientstatus (status) VALUES ('new')")
con.execute("INSERT INTO clientstatus (status) VALUES ('good')")
con.execute("INSERT INTO clientstatus (status) VALUES ('bad')")
#Populate frame status table
con.execute("INSERT INTO framestatus (status) VALUES ('empty')")
con.execute("INSERT INTO framestatus (status) VALUES ('draft')")
con.execute("INSERT INTO framestatus (status) VALUES ('running')")
con.execute("INSERT INTO framestatus (status) VALUES ('done')")
#Populate project status table
con.execute("INSERT INTO projectstatus (status) VALUES ('stopped')")
con.execute("INSERT INTO projectstatus (status) VALUES ('running')")
con.execute("INSERT INTO projectstatus (status) VALUES ('complete')")
#Populate frametypes table - just some basic values; fix later.
con.execute("INSERT INTO frametypes (ext, name) VALUES ('png','PNG')")
con.execute("INSERT INTO frametypes (ext, name) VALUES ('jpg','JPEG')")
con.execute("INSERT INTO frametypes (ext, name) VALUES ('exr','OpenEXR')")
#For testing purposes, create dummy projects.
con.execute("INSERT INTO wishes (name, majorversion, minorversion, status, frametype, engine) VALUES ('wish1', '2', '73', 'stopped', 1, 'cycles')") 
con.execute("INSERT INTO wishes (name, majorversion, minorversion, status, frametype, engine) VALUES ('wish2', '2', '73', 'running', 2, 'internal')") 
#Populate table of user-editable fields - anything with value "1" is user-editable.
con.execute("INSERT INTO userfields (tableid, field, editable) VALUES ('blendfiles', 'filename',      1)")
con.execute("INSERT INTO userfields (tableid, field, editable) VALUES ('wishes',     'name',          1)")
con.execute("INSERT INTO userfields (tableid, field, editable) VALUES ('wishes',     'majorversion',  1)")
con.execute("INSERT INTO userfields (tableid, field, editable) VALUES ('wishes',     'minorversion',  1)")
con.execute("INSERT INTO userfields (tableid, field, editable) VALUES ('wishes',     'versionsuffix', 1)")
con.execute("INSERT INTO userfields (tableid, field, editable) VALUES ('wishes',     'status',        1)")
con.execute("INSERT INTO userfields (tableid, field, editable) VALUES ('wishes',     'frametype',     1)")
con.execute("INSERT INTO userfields (tableid, field, editable) VALUES ('wishes',     'firstframe',    1)")
con.execute("INSERT INTO userfields (tableid, field, editable) VALUES ('wishes',     'lastframe',     1)")
con.execute("INSERT INTO userfields (tableid, field, editable) VALUES ('wishes',     'engine',        1)")
con.commit()
