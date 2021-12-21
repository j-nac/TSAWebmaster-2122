$(document).ready(function() {
    const socket = io.connect('ws://localhost:5000');

    socket.on('connect', function() {
        socket.send('user connected');
    });

    socket.on('message', function(msg) {
        $('#messages').append('<li>'+msg+'</li>');
    });
});