from logging import debug
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit, send
import cv2
import io
import base64


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)
    
@socketio.on('connect')
def test_connect():
    # emit('my response', {'data': 'Connected'})
    send("This is sever speaking!!")
    send_image()
    print("Connected!!")

@socketio.on("message")
def message(data):
    print(data)

@socketio.on("json")
def handle_json(json):
    print(json)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.event('imageS2C')
def send_image():
    print("[ Attempting to send Image...]")
    with open("static/selfie1.jpg", 'rb') as f:
        image_data = f.read()

    emit('imageS2C', {"image": True, "buffer":image_data})
    # print(image_data)


@socketio.on('imageC2S')
def handle_image(info):
    print("[Recieving from Client]")
    with open("recieved.jpg", "wb") as f:
        f.write(base64.b64decode(info.split(',')[1]))

    
if __name__ == '__main__':
    socketio.run(app, debug=True)
