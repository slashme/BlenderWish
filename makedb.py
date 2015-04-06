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
  name TEXT NOT NULL,
  editable INTEGER NOT NULL,
  FOREIGN KEY(tableid) REFERENCES alltables(name)
  )
''')
#Populate engines table
con.execute("INSERT INTO engines (name) VALUES ('cycles')")
con.execute("INSERT INTO engines (name) VALUES ('internal')")
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
con.execute("INSERT INTO frametypes (ext, name) VALUES ('png','PNG')")
con.execute("INSERT INTO frametypes (ext, name) VALUES ('jpg','JPEG')")
con.execute("INSERT INTO frametypes (ext, name) VALUES ('exr','OpenEXR')")
#For testing purposes, create dummy projects.
con.execute("INSERT INTO wishes (name, majorversion, minorversion, status, frametype, engine) VALUES ('wish1', '2', '73', 1, 1, 1)") 
con.execute("INSERT INTO wishes (name, majorversion, minorversion, status, frametype, engine) VALUES ('wish2', '2', '73', 2, 2, 2)") 
#Populate table of tables
con.execute("INSERT INTO alltables (name) VALUES ('projectstatus')")
con.execute("INSERT INTO alltables (name) VALUES ('clientstatus')")
con.execute("INSERT INTO alltables (name) VALUES ('framestatus')")
con.execute("INSERT INTO alltables (name) VALUES ('clients')")
con.execute("INSERT INTO alltables (name) VALUES ('frametypes')")
con.execute("INSERT INTO alltables (name) VALUES ('blendfiles')")
con.execute("INSERT INTO alltables (name) VALUES ('frames')")
con.execute("INSERT INTO alltables (name) VALUES ('engines')")
con.execute("INSERT INTO alltables (name) VALUES ('wishes')")
con.execute("INSERT INTO alltables (name) VALUES ('alltables')")
con.execute("INSERT INTO alltables (name) VALUES ('userfields')")
#Populate table of user-editable fields - anything with value "1" is user-editable.
con.execute("INSERT INTO userfields (tableid, name, editable) VALUES ('tableid', 'field', 1)")
blendfiles', 'filename
    wishes', 'name
    wishes', 'majorversion
    wishes', 'minorversion
    wishes', 'versionsuffix
    wishes', 'status
    wishes', 'frametype
    wishes', 'firstframe
    wishes', 'lastframe
    wishes', 'engine
''')
con.commit()
