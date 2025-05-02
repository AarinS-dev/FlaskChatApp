from flask import Flask, render_template
from flask_socketio import SocketIO, send
from pydantic import BaseModel, validator, ValidationError

app = Flask(__name__)
socketio = SocketIO(app)

class Messagehandler(BaseModel):
    message: str
    @validator('message')
    def no_hash_symbol(cls, v):
        if '#' in v:
            raise ValueError("message cannot contain #")
        return v

@app.route("/")
def Homemessage():
    return render_template('home.html')

@socketio.on('message')
def handle_message(msg):
    try: 
        validated = Messagehandler(message=msg)
        print("Received:", validated.message)
        send(validated.message, broadcast=True)
    except ValidationError as e:
        print("validation failed", e)
        send("Invalid Message: '#' is not allowed", broadcast=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)
