from flask import Flask, render_template, redirect

from socketio_app import socketio  # Importando o objeto socketio
from socket_handler import handle_message

app = Flask(__name__)

# Associando a instância do SocketIO à aplicação Flask
socketio.init_app(app)

@app.route('/')
def home():
    return redirect('/chat')  # Redireciona diretamente para a página de chat



@app.route('/chat')
@app.route('/chat/')

def chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message_event(message):
    handle_message(message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
