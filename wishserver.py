import sqlite3
from bottle import Bottle, route, get, post, request, run, template, debug

app = Bottle()

@app.route('/list') 
def list():
  conn = sqlite3.connect('wishes.db')
  c = conn.cursor()
  c.execute('''
  SELECT
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
  result = [(u'Project name', u'Status', u'Frame type', u'Engine')] + result
  c.close()
  output = template('make_table', rows=result)
  return output

def showproj(wishid):
  conn = sqlite3.connect('wishes.db')
  c = conn.cursor()
  c.execute('''
  SELECT
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
    output = template('not_found', message='Project %s not found'%wishid)
  else:
    result = [(u'Project name', u'Status', u'Frame type', u'Engine')] + result
    c.close()
    output = template('proj_detail', rows=result)
  return output
  

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
    return template('not_found', message='Project %s not found'%wishname)
  else:
    return showproj(result[0][0])

debug(True)
run(app, host='localhost', port=8080, reloader=True)
