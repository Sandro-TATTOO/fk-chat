from flask_socketio import emit

def handle_message(message):
    emit('message', message, broadcast=True)
