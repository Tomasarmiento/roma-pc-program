const socket = new WebSocket("ws://127.0.0.1:8000/ws/front/");
    socket.addEventListener("open", function (event) {
        socket.send(
          JSON.stringify({
            message: "datos",      
          })
        );
    });
    // Escucha cierre de WebSocket
    socket.onclose = function (event) {
        window.location.reload();
      };

      window.addEventListener("hashchange", () => {                  //cuando tocas f5
        (window.location.hash);
    });

    window.addEventListener("DOMContentLoaded", () => {                         //todo el tiempo
        (window.location.hash);
        console.log("Enter main js");
    });


socket.onmessage = function (event) {
    console.log('aca');
    const datosWs = JSON.parse(event.data);
    console.log(datosWs);
};