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
    var present_error = false
    

    const datosWs = JSON.parse(event.data);
    console.log(datosWs.plc_sensors[".init_error"]);
    // console.log(datosWs.mensajes_log[0]);
    // if (datosWs.mensajes_log[0] == "error emergencia activa") {
    //   console.log('es igual');
      
    // }
    const hash_manual = document.getElementById("manual_hash")

    if (datosWs.plc_sensors[".pause_auto"] == true && datosWs.plc_sensors[".pause_semi"] == true){
      hash_manual.className = "nav-link"
    }
    else {
      hash_manual.className = "nav-link disabled"
    }

    step = document.getElementById("errores_hash")
      for (let i = 0; i <= datosWs.mensajes_log.length-1;i++){
          // console.log(datosWs.mensajes_log[i].length);
          if (datosWs.mensajes_log[i].length > 0) {
            step.style.color = "red"
            present_error = true
          } else {
            // step.style.color = ""
          }
      }

      if (present_error == false) {
        step.style.color = ""
      }


    if (document.getElementById("salidaDeTexto")) {
      if (datosWs.mensajes_log.length > 0) {
        listaMensajes = [];
        if (sessionStorage.getItem("mensajes")){
          window.sessionStorage.removeItem("mensajes")
        }
        listaMensajes.push(datosWs.mensajes_log);
        sessionStorage.setItem("mensajes", listaMensajes);
        InsertarTexto(datosWs.mensajes_log);
      };
    }

    if (document.getElementById("salidaDeTextoHistorico")) {
      if (datosWs.mensajes_error_log.length > 0) {
        listaMensajesHistorico = [];
        if (sessionStorage.getItem("mensajesHistorico")){
          window.sessionStorage.removeItem("mensajesHistorico")
        }
        listaMensajesHistorico.push(datosWs.mensajes_error_log);
        sessionStorage.setItem("mensajesHistorico", listaMensajesHistorico);
        InsertarTextoHistorico(datosWs.mensajes_error_log);
      };
    }

    switch (window.location.pathname) {
      case "/semiAutomatico/":
        semiAutomatico(datosWs)
        sensores(datosWs)
        break
      case "/okuma_1_neumatic/":
        sensores(datosWs)
        break
      case "/mesa_1_neumatic/":
        sensores(datosWs)
        break
      case "/automatico/":
        auto_step(datosWs)
        break
      case "/desactivar_okuma/":
        disable_ch(datosWs)
        break
    }
  };