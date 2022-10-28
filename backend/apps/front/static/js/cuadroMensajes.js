var listaMensajes = [];

window.addEventListener("DOMContentLoaded", () => {                         //todo el tiempo
    (window.location.hash);
    monitor = document.querySelector("#component-monitor");
    cuadroDeTextoIndex = document.querySelector("#terminalDeTexto");
    if (sessionStorage.getItem("mensajes") && cuadroDeTextoIndex) {
        let ul = document.getElementById("cuadroMensajes");
        const listaMensajes = sessionStorage.getItem("mensajes").split(",").reverse();
        for (let i = 0; i < listaMensajes.length; i++) {
            const li = document.createElement("li");
            li.setAttribute("style", "list-style: none;");
            li.innerHTML = listaMensajes[i];
            ul.appendChild(li);
        }
    }
});

function InsertarTexto(datosWs) {
  if (document.getElementById("cuadroMensajes")) {

    let ul = document.getElementById("cuadroMensajes");

    while(ul.firstChild){
      ul.removeChild(ul.firstChild)

    }

    // document.getElementById("cuadroMensajes").remove()
    // g = document.createElement("ul")
    // g.setAttribute("id","cuadroMensajes" )

    // cuadroDeTextoIndex = document.querySelector("#terminalDeTexto");
    // if (sessionStorage.getItem("mensajes") && cuadroDeTextoIndex) {
    //     let ul = document.getElementById("cuadroMensajes");
    //     const listaMensajes = sessionStorage.getItem("mensajes").split(",").reverse();
    //     for (let i = 0; i < listaMensajes.length; i++) {
    //         const li = document.createElement("li");
    //         li.setAttribute("style", "list-style: none;");
    //         li.innerHTML = listaMensajes[i];
    //         ul.appendChild(li);
    //     }
    // }

  }
    var ul = document.getElementById("cuadroMensajes");
    if (ul){
      for (let i = 0; i < datosWs.length; i++) {
          const li = document.createElement("li");
          li.setAttribute("style", "list-style: none;" );
          li.innerHTML = datosWs[i];
          ul.prepend(li);
      }
    }
    else{
      console.log('No hay mensaje');
    }
  }

socket.onmessage = function (event) {
    const datosWs = JSON.parse(event.data);
    // console.log(datosWs);

    if (datosWs.mensajes_log.length > 0) {
        listaMensajes = [];
        if (sessionStorage.getItem("mensajes")){
          console.log("borro mensaje");
          window.sessionStorage.removeItem("mensajes")
          // sessionStorage.removeItem("mensajesError");
          sessionStorage.setItem("mensajesError", listaMensajes);
        }
        listaMensajes.push(datosWs.mensajes_log);
        sessionStorage.setItem("mensajes", listaMensajes);
        InsertarTexto(datosWs.mensajes_log);
      };
}