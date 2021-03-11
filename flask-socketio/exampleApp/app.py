from logging import debug
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import cv2
import io


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

@socketio.event('image')
def send_image():
    # img = cv2.imread("static/selfie1.jpg")
    # isSuccessful, buffer = cv2.imencode(".jpg", img)
    # io_buf = io.BytesIO(buffer)
    # print("Inside image event!")
    with open("static/selfie1.jpg", 'rb') as f:
        image_data = f.read()
    emit('image', {"image": True, "buffer":str(image_data)})


if __name__ == '__main__':
    socketio.run(app, debug=True)
