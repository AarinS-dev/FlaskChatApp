from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def Homemessage():
    return render_template('home.html')

@socketio.on('message')
def handle_message(msg):
    print("Recieved:", msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)