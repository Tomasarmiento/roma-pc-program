var listaMensajes = [];

window.addEventListener("DOMContentLoaded", () => {                         //todo el tiempo
    (window.location.hash);
    cuadroDeTextoIndexHistorico = document.querySelector("#terminalDeTextoHistorico");
    if (sessionStorage.getItem("mensajesHistorico") && cuadroDeTextoIndexHistorico) {
        let ul = document.getElementById("cuadroMensajesHistorico");
        const listaMensajes = sessionStorage.getItem("mensajesHistorico").split(",").reverse();
        for (let i = 0; i < listaMensajes.length; i++) {
            const li = document.createElement("li");
            li.setAttribute("style", "list-style: none;");
            li.innerHTML = listaMensajes[i];
            ul.appendChild(li);
        }
    }
});

function InsertarTextoHistorico(datosWs) {
  if (document.getElementById("cuadroMensajesHistorico")) {

    let ul = document.getElementById("cuadroMensajesHistorico");

    while(ul.firstChild){
      ul.removeChild(ul.firstChild)

    }

    // document.getElementById("cuadroMensajesHistorico").remove()
    // g = document.createElement("ul")
    // g.setAttribute("id","cuadroMensajesHistorico" )

    // cuadroDeTextoIndex = document.querySelector("#terminalDeTexto");
    // if (sessionStorage.getItem("mensajesHistorico") && cuadroDeTextoIndex) {
    //     let ul = document.getElementById("cuadroMensajesHistorico");
    //     const listaMensajes = sessionStorage.getItem("mensajesHistorico").split(",").reverse();
    //     for (let i = 0; i < listaMensajes.length; i++) {
    //         const li = document.createElement("li");
    //         li.setAttribute("style", "list-style: none;");
    //         li.innerHTML = listaMensajes[i];
    //         ul.appendChild(li);
    //     }
    // }

  }
    var ul = document.getElementById("cuadroMensajesHistorico");
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

