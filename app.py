from flask import Flask, render_template
from flask_socketio import SocketIO
from socketio_app import socketio  # Importando o objeto socketio
from socket_handler import handle_message

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat')
@app.route('/chat/pro')

def chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message_event(message):
    handle_message(message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
