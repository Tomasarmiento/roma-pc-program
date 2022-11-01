// const socket = new WebSocket("ws://192.168.3.127:8000/ws/front/");//"ws://127.0.0.1:8000/ws/front/"
const socket = new WebSocket("ws://127.0.0.1:8000/ws/front/");//"ws://127.0.0.1:8000/ws/front/"
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
    const datosWs = JSON.parse(event.data);
    // console.log(datosWs.plc_sensors.R_I_AUT_SEM);
    // console.log(datosWs.plc_sensors);
    // console.log(datosWs);
    switch (window.location.pathname) {
      case "/semiAutomatico/":
        semiAutomatico(datosWs)
      case "/semiAutomatico/":
        sensores(datosWs)
      case "/okuma_1_neumatic/":
        sensores(datosWs)
      case "/mesa_1_neumatic/":
        sensores(datosWs)
      // case "/automatico/":
      //   auto_step(datosWs)
    }
  };


