# Flask SocketIO
Flask-SocketIO gives Flask applications access to low latency bi-directional communications between the clients and the server. The client-side application can use any of the [SocketIO](socket.io) official clients libraries in Javascript, C++, Java and Swift, or any compatible client to establish a permanent connection to the server.


# To communicate with JS :
You can find the documentation [Here](https://socket.io/docs/v3).
Please import socket in js:

```
<script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js" integrity="sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I=" crossorigin="anonymous"></script>
```

Then create an instance of the socket to work with:
```
    var socket = io();
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
```

### Event Handlers:
The sockets communicate via events and transfer data according to the custom or predefined event declared.
Some of them are:
- 'message' : sends the data in string format
- 'json' : sends the data in json format
- "CUSTOM EVENTS" : These events can handle as many arguements as you want.

A custom event can be defined in following ways:
Way1:
```
    @socketio.on('custom_event1')
    def handle_my_custom_event1(arg1, arg2, arg3):
        print(arg1, arg2, arg3)
```

Way 2: It takes the event name from the function.
```
    @socketio.event
    def handle_my_custom_event2(data):
        print(data)
```

Way 3: After defining a fnc
```
    def my_function_handler(data):
        pass
    
    socketio.on('my event', my_function_handler, namespace='/test')
```

### Sending data to the other end
This can be done in two ways:
- `send` : This by defaults sends the string or the provided data to the **message** event Bucket list.
  ``` send(data)```
- `emit` : This requires us defining of the event to which the data will be passed on to.
  ``` emit('custom_event', data)```

The other side should recieve the data through the same event:
For example sending the data to JS frontend client from server.
```
socket.on('custom_event', (data)=>{
    console.log(data); // this prints the data sent from server to client.
})
```

There are many other things that can be done via websockets i.e. private messaging, creating rooms, joining them, leaving them and sending broadcast messages(messaging all clients connected to that server) as well.