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
  result = [(u'Project name', u'Status', u'Frame type', u'Engine')] + result
  c.close()
  output = template('make_table', rows=result)
  return output
  

@app.route('/wish/<wishid:int>') #Try a number, if it fails try a name, else give a 404.
def showprojbynum(wishid):
  return showproj(wishid)

@app.route('/wish/<wishname>') #Try a number, if it fails try a name, else give a 404.
def showprojbyname(wishname):
  conn = sqlite3.connect('wishes.db')
  c = conn.cursor()
  c.execute("SELECT wishid FROM wishes WHERE name = ?", (wishname,))
  data=c.fetchall()
  if len(data)==0:
    return('Project %s not found'%wishname)
  else:
    return showproj(data[0][0])

debug(True)
run(app, host='localhost', port=8080, reloader=True)
