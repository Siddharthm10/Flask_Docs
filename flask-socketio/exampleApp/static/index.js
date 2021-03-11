
$(document).ready(function() {
    // Connect to the Socket.IO server.
    // The connection URL has the following format, relative to the current page:
    //     http[s]://<domain>:<port>[/<namespace>]
    var socket = io();
    var img = $("#input");
    var data = {
        "employee":{ "name":"John", "age":30, "city":"New York" }
        };

    // Event handler for new connections.
    // The callback function is invoked when a connection with the
    // server is established.
    socket.on('connect', function() {
        console.log("Connected!!")
        socket.send("THIS IS FUCKING CONNECTED!!")
        socket.emit('json', data)
    });

    socket.on('image', function(info){
        console.log("image recieved!!")
        console.log(info.image);
        console.log(info.buffer);
        img.src = 'data:image/jpeg;base64,' + info.buffer;
    })

    socket.on('message', (data)=>{
        console.log(data);
    })
});
