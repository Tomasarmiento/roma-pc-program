window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    const btn_desactivate_okuma_1 = document.getElementById('desactivate_ok1')
    const btn_desactivate_okuma_2 = document.getElementById('desactivate_ok2')
    const btn_desactivate_okuma_3 = document.getElementById('desactivate_ok3')
    const btn_desactivate_okuma_4 = document.getElementById('desactivate_ok4')

    const btn_desactivate_mesa_1 = document.getElementById('desactivate_me1')
    const btn_desactivate_mesa_2 = document.getElementById('desactivate_me2')

    btn_desactivate_mesa_1.addEventListener('click', (e) => {
        disable_okuma('mesa_armado_1')
    });

    btn_desactivate_mesa_2.addEventListener('click', (e) => {
        disable_okuma('mesa_armado_2')
    });

    btn_desactivate_okuma_1.addEventListener('click', (e) => {
        disable_okuma('okuma_1')
    });

    btn_desactivate_okuma_2.addEventListener('click', (e) => {
        disable_okuma('okuma_2')
    });

    btn_desactivate_okuma_3.addEventListener('click', (e) => {
        disable_okuma('okuma_3')
    });

    btn_desactivate_okuma_4.addEventListener('click', (e) => {
        disable_okuma('okuma_4')
    });

    function disable_okuma(model_machine){
        let url = "http://localhost:8000/control/automatico/okuma/";
        let params = "model_machine=" + model_machine;
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }

});

socket.onmessage = function (event) {
    // console.log('aca');
    const datosWs = JSON.parse(event.data);
    // console.log(datosWs);
    //BLOQUES DE HABILITACION PARA OKUMAS
    const cuadrado_mesa1 = document.getElementById("cuadrado_mesa1")
    const cuadrado_mesa2 = document.getElementById("cuadrado_mesa2")
    const cuadrado_okuma1 = document.getElementById("cuadrado_okuma1")
    const cuadrado_okuma2 = document.getElementById("cuadrado_okuma2")
    const cuadrado_okuma3 = document.getElementById("cuadrado_okuma3")
    const cuadrado_okuma4 = document.getElementById("cuadrado_okuma4")

    datosWs.mesa_armado_1 == 1
    ? (cuadrado_mesa1.className = "cuadrado_mesa1 cuadrado_green")
    : (cuadrado_mesa1.className = "cuadrado_mesa1 cuadrado_red")

    datosWs.mesa_armado_2 == 1
    ? (cuadrado_mesa2.className = "cuadrado_mesa2 cuadrado_green")
    : (cuadrado_mesa2.className = "cuadrado_mesa2 cuadrado_red")

    datosWs.okuma_1 == 1
    ? (cuadrado_okuma1.className = "cuadrado_okuma1 cuadrado_green")
    : (cuadrado_okuma1.className = "cuadrado_okuma1 cuadrado_red")
    
    datosWs.okuma_2 == 1
    ? (cuadrado_okuma2.className = "cuadrado_okuma2 cuadrado_green")
    : (cuadrado_okuma2.className = "cuadrado_okuma2 cuadrado_red")

    datosWs.okuma_3 == 1
    ? (cuadrado_okuma3.className = "cuadrado_okuma3 cuadrado_green")
    : (cuadrado_okuma3.className = "cuadrado_okuma3 cuadrado_red")

    datosWs.okuma_4 == 1
    ? (cuadrado_okuma4.className = "cuadrado_okuma4 cuadrado_green")
    : (cuadrado_okuma4.className = "cuadrado_okuma4 cuadrado_red")

}; 