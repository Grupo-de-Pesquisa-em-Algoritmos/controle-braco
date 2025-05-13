from flask import Flask 
from flask_socketio import SocketIO, emit
from control import run_movement
from threading import Lock

app = Flask(__name__, static_url_path='')
socketio = SocketIO(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

mutex = Lock()

@socketio.on('mov')
def handle_msg(data):
    if type(data['motor']) is str:
        return

    if mutex.acquire(blocking=False):
        try:
            run_movement(data['motor'], data['amnt'], data['mov_all'])
        finally:
            mutex.release()

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
