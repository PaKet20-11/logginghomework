from bottle import Bottle, request

SERVER_URL = "https://logginghomework.herokuapp.com"

app = Bottle()

@app.route('/success')
def success():
    return "200 OK"

@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")

app.run(host='localhost', port=8080)