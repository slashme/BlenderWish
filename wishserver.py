from bottle import Bottle, get, post, request, run, template

app = Bottle()

@app.get('/login') 
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.post('/login') 
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('<p>Your username was {{username}}.</p> <p>Your password was {{password}}.</p>', username=username, password=password )

run(app, host='localhost', port=8080)
