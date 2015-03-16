import sqlite3
from bottle import Bottle, route, get, post, request, run, template, debug

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
    projectstatus.name AS status_name,
    frametypes.name AS frametype_name,
    engines.name AS engine_name
  FROM 
    wishes 
    LEFT JOIN projectstatus ON wishes.status = projectstatus.statusid
    LEFT JOIN frametypes ON wishes.frametype = frametypes.frametypeid
    LEFT JOIN engines ON wishes.engine = engines.engineid
  ''')
  result = c.fetchall()
  result = [(u'', u'Project name', u'Status', u'Frame type', u'Engine')] + result
  c.close()
  output = template('make_table', rows=result, title="Wish list")
  return output

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
  pn=request.forms.get('wish_name')
  ft=request.forms.get('ft')
  en=request.forms.get('en')
  maj_ver=request.forms.get('maj_ver')
  min_ver=request.forms.get('min_ver')
  ver_suf=request.forms.get('ver_suf')
  fr1=request.forms.get('fr1')
  frn=request.forms.get('frn')
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

debug(True)
run(app, host='localhost', port=8080, reloader=True)
