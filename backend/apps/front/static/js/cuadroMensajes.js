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

