
from flask_socketio import emit
from .extensions import socketio

@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('user_join')
def handle_user_join(data):
    username = data.get('username')
    print(f'{username} has joined the chat')

@socketio.on('send_message')
def handle_send_message(data):
    username = data.get('username')
    message = data.get('message')
    print(f'Message from {username}: {message}')
    emit('chat', {'username': username, 'message': message}, broadcast=True)