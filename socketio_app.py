from flask_socketio import SocketIO

socketio = SocketIO()  # Apenas cria a instância do SocketIO

# Aqui você pode definir os eventos do Socket.IO
def handle_message(message):
    # Lógica para lidar com a mensagem
    pass
