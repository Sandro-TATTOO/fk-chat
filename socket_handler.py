from flask_socketio import emit
from socketio_app import socketio  # Importando o objeto socketio

def handle_message(message):
    emit('message', message, broadcast=True)

@socketio.on('set_nickname')
def set_nickname(nickname):
    emit('nickname', nickname, broadcast=True)


@socketio.on('image')
def handle_image(image_blob):
    emit('image', image_blob, broadcast=True)
