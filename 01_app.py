from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@sock.route('/reverse')
def reverse(ws):
    while True:
        data = ws.receive()
        if data is None:
            break
        ws.send(data[::-1])

# FLASK_APP=01_app.py flask run
# wscat --connect http://127.0.0.1:5000/reverse