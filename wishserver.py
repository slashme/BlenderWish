import sqlite3, os, errno
from bottle import Bottle, route, get, post, request, run, template, debug, error

app = Bottle()

def showproj(wishid):
  conn = sqlite3.connect('wishes.db')
  c = conn.cursor()
  c.execute('''
  SELECT
    wishes.wishid AS wish_id, 
    wishes.name AS wish_name, 
    projectstatus.name AS status_name,
    frametypes.name AS frametype_name,
    engines.name AS engine_name
  FROM 
    wishes
    LEFT JOIN projectstatus ON wishes.status = projectstatus.statusid
    LEFT JOIN frametypes ON wishes.frametype = frametypes.frametypeid
    LEFT JOIN engines ON wishes.engine = engines.engineid
    WHERE wishes.wishid = ?
  ''', (wishid,))
  result = c.fetchall()
  if len(result)==0:
    output = template('not_found', message='Project %s not found'%wishid, title='Unwished')
  else:
    result = [(u'', u'Project name', u'Status', u'Frame type', u'Engine')] + result
    c.close()
    output = template('make_table', rows=result, title='Project %s'%result[1][0])
  return output
  
@app.route('/list') #List projects
def list():
  conn = sqlite3.connect('wishes.db')
  c = conn.cursor()
  c.execute('''
  SELECT
    wishes.wishid AS wish_id, 
    wishes.name AS wish_name, 
    projectstatus.name AS status_name
  FROM 
    wishes 
    LEFT JOIN projectstatus ON wishes.status = projectstatus.statusid
  ''')
  result = c.fetchall()
  result = [(u'', u'Project name', u'Status')] + result
  c.close()
  output = template('make_table', rows=result, title="Wish list")
  return output

#In progress: start
@app.get('/wish/<wishid:int>/projupload') #Upload a blender project file
def projupload(wishid):
  #Check if the wish ID is valid
  conn = sqlite3.connect('wishes.db')
  c = conn.cursor()
  c.execute("SELECT wishid, name FROM wishes WHERE wishid = ?", (wishid,))
  wishidlist = c.fetchall() #This should have length 1
  if len(wishidlist)==0:
    return template('not_found', message='Project %s not found'%wishid, title="Unwished")
  #Get the upload time of the blend file. This will have length 1 if we're asked to overwrite a file, otherwise 0
  c.execute("SELECT uploadtime FROM blendfiles WHERE wishid = ?", (wishid,))
  uploadtimelist = c.fetchall()
  c.close()
  #Generate title text explaining to the user whether this will upload an existing file or create a new one.
  if len(uploadtimelist)==1:
    titletext = "Upload over blend file uploaded on " + uploadtimelist[0][0] + " for project " + wishidlist[0][1]
  else:
    #return template('not_found', message=str(wishidlist), title="Debugging") #Debug: testing
    titletext = "Upload blend file for project" + " for project " + wishidlist[0][1]
  uploadaction="/wish/" + str(wishid) + "/projupload" #set form action variable
  wishform = template('single_upload', uploadaction=uploadaction, title=titletext) #Generate a file upload form
  return wishform

@app.post('/wish/<wishid:int>/projupload') #Upload a blender project file : post action
def do_projupload(wishid):
  upload=request.files.get('upload')
  #If we don't yet have a directory for the project, create it:
  projpath = os.path.dirname(__file__) + str(wishid) + "/"
  try:
    os.mkdir(projpath)
  except OSError as exc:
    if exc.errno != errno.EEXIST:
      raise #Do I need to handle this more gracefully?
  upload.save(destination=projpath + str(wishid) + ".blend", overwrite=True) #Maybe warn?
  #Now update the database:
  #Find out whether the file already is listed. If so, just update the upload time and filename.
  #If the file is not listed, insert into blendfiles table.
#  conn = sqlite3.connect('wishes.db')
#  c = conn.cursor()
#  c.execute('''
#  INSERT INTO wishes(name, majorversion, minorversion, versionsuffix, status, frametype, firstframe, lastframe, engine)
#  VALUES 
#    (?, ?, ?, ?, ?, ?, ?, ?, ?)
#  ''', (pn, maj_ver, min_ver, ver_suf, 1, ft, fr1, frn, en))
#  new_wish_id = c.lastrowid
#  conn.commit()
#  c.close()
  return list() #Just return something for now...
#In progress: end

@app.get('/makewish') #Create a new project: get action
def makewish():
  #Get the list of allowed frametypes to insert into the template.
  conn = sqlite3.connect('wishes.db')
  c = conn.cursor()
  c.execute("SELECT frametypeid, name FROM frametypes")
  frametypelist = c.fetchall()
  c.execute("SELECT engineid, name FROM engines")
  enginelist = c.fetchall()
  c.close()
  wishform = template('wish_form', enginelist=enginelist, frametypelist=frametypelist, title="Make a Blender wish") #Generate a form with pre-populated option lists.
  return wishform

@app.post('/makewish') #Create a new project: post action
def do_makewish():
  pn=request.forms.getunicode('wish_name')
  ft=request.forms.getunicode('ft')
  en=request.forms.getunicode('en')
  maj_ver=request.forms.getunicode('maj_ver')
  min_ver=request.forms.getunicode('min_ver')
  ver_suf=request.forms.getunicode('ver_suf')
  fr1=request.forms.getunicode('fr1')
  frn=request.forms.getunicode('frn')
  conn = sqlite3.connect('wishes.db')
  c = conn.cursor()
  c.execute('''
  INSERT INTO wishes(name, majorversion, minorversion, versionsuffix, status, frametype, firstframe, lastframe, engine)
  VALUES 
    (?, ?, ?, ?, ?, ?, ?, ?, ?)
  ''', (pn, maj_ver, min_ver, ver_suf, 1, ft, fr1, frn, en))
  new_wish_id = c.lastrowid
  conn.commit()
  c.close()
  return showproj(new_wish_id)

@app.route('/wish/<wishid:int>') #Return the project by number - showproj will redirect if not valid ID.
def showprojbynum(wishid):
  return showproj(wishid)

@app.route('/wish/<wishname>') #If valid project name, find the number and run showproj, else redirect.
def showprojbyname(wishname):
  conn = sqlite3.connect('wishes.db')
  c = conn.cursor()
  c.execute("SELECT wishid FROM wishes WHERE name = ?", (wishname,))
  result=c.fetchall()
  if len(result)==0:
    return template('not_found', message='Project %s not found'%wishname, title="Unwished")
  else:
    return showproj(result[0][0])

@app.error(404)
def error404(error):
    return list()

debug(True)
run(app, host='localhost', port=8080, reloader=True)
