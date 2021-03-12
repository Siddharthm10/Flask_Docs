
$(document).ready(function() {
    // Connect to the Socket.IO server.
    // The connection URL has the following format, relative to the current page:
    //     http[s]://<domain>:<port>[/<namespace>]
    var socket = io();
    var img = document.querySelector('#input');
    // var im2 = document.querySelector('#output');
    var ctx = document.querySelector('#idhar').getContext('2d');

    // Event handler for new connections.
    // The callback function is invoked when a connection with the
    // server is established.
    socket.on('connect', function() {
        console.log("Connected!!");
        // socket.emit('json', data);
    });

    socket.on('imageS2C', function(info){
        console.log("image recieved!!")
        console.log(info.image);
        console.log(info.buffer);
        console.log(info);

        $("#input").attr("src","data:image/png;base64,"+b64(info.buffer));
        // var bytes = new Uint8Array(info.buffer);    
        // console.log(bytes)    
        
        // document.getElementById('input').src = URL.createObjectURL(
        //     new Blob([bytes.buffer], { type: 'image/jpeg' } /* (1) */)
        // );

        // $("#input").attr("src", 'data:image/jpeg;base64,' + info.buffer);
        // ctx.drawImage(img, 0, 0);
        // console.log("Canvas Drawn!!")




        // var blob = new Blob([bytes.buffer]);
        // console.log(blob);
        // urlObject = URL.createObjectURL(blob);
        // img.src = urlObject;
        
        // if (urlObject) {
        //     URL.revokeObjectURL(urlObject) // only required if you do that multiple times
        // }
        
        // This is working part of code which shows a red dot in the center.
        // const content = new Uint8Array([137, 80, 78, 71, 13, 10, 26, 10, 0, 0, 0, 13, 73, 72, 68, 82, 0, 0, 0, 5, 0, 0, 0, 5, 8, 6, 0, 0, 0, 141, 111, 38, 229, 0, 0, 0, 28, 73, 68, 65, 84, 8, 215, 99, 248, 255, 255, 63, 195, 127, 6, 32, 5, 195, 32, 18, 132, 208, 49, 241, 130, 88, 205, 4, 0, 14, 245, 53, 203, 209, 142, 14, 31, 0, 0, 0, 0, 73, 69, 78, 68, 174, 66, 96, 130]);
        // console.log(content)
        // document.getElementById('input').src = URL.createObjectURL(
        //     new Blob([content.buffer], { type: 'image/png' } )
        // );
        console.log("Logging recieved!!")
        console.log(img.src);
        socket.emit('imageC2S', img.src);
        p = document.createElement("P");
        p.innerHTML = img.src;
        document.getElementById("myDIV").appendChild(p);  
    })

    

    socket.on('message', (data)=>{
        console.log(data);
    })
});

function b64(e){
    var t="";
    var n=new Uint8Array(e);
    var r=n.byteLength;
    for(var i=0;i<r;i++){
        t+=String.fromCharCode(n[i])
    }
    return window.btoa(t)
}
