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
  c.close()
  output = template('make_table', rows=result)
  return output

debug(True)
run(app, host='localhost', port=8080, reloader=True)
