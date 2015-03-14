import sqlite3
from bottle import Bottle, route, get, post, request, run, template, debug

app = Bottle()

@app.route('/list') 
def list():
    conn = sqlite3.connect('wishes.db')
    c = conn.cursor()
    c.execute("SELECT wishid, name FROM wishes")
    result = c.fetchall()
    return str(result)

debug(True)
run(app, host='localhost', port=8080, reloader=True)
