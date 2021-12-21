from flask_socketio import SocketIO, send
from app import socketio

@socketio.on('message')
def message_handler(msg):
    if msg == 'user connected':
        send('[Fred] Hello')
        send('[Fred] I am Fred, your friendly FAQ bot here to help')
        send('[Fred] What can I do for you?')