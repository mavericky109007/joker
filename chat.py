from flask_socketio import SocketIO, emit
from flask import Flask

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

class ChatService:
    @socketio.on('join_room')
    def handle_join(data):
        username = data['username']
        room = data['room']
        # Join room logic
        emit('user_joined', {'username': username}, room=room)
    
    @socketio.on('send_message')
    def handle_message(data):
        # Message broadcasting logic
        emit('receive_message', data, room=data['room'])
