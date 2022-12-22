window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    
    const btn_me1_disable = document.getElementById("btn_me1_disable")
    const btn_ch1_disable = document.getElementById("btn_ch1_disable")
    const btn_ch2_disable = document.getElementById("btn_ch2_disable")
    const btn_ch3_disable = document.getElementById("btn_ch3_disable")
    const btn_ch4_disable = document.getElementById("btn_ch4_disable")

    

    
    

    btn_me1_disable.addEventListener("click", (e) => {
        menu = btn_me1_disable.getAttribute('menu');
        cmd = btn_me1_disable.getAttribute('cmd');
        sendCommandDisableCh(menu, cmd);
    });
    
    btn_ch1_disable.addEventListener("click", (e) => {
        menu = btn_ch1_disable.getAttribute('menu');
        cmd = btn_ch1_disable.getAttribute('cmd');
        sendCommandDisableCh(menu, cmd);
    });
    
    btn_ch2_disable.addEventListener("click", (e) => {
        menu = btn_ch2_disable.getAttribute('menu');
        cmd = btn_ch2_disable.getAttribute('cmd');
        sendCommandDisableCh(menu, cmd);
    });
    
    btn_ch3_disable.addEventListener("click", (e) => {
        menu = btn_ch3_disable.getAttribute('menu');
        cmd = btn_ch3_disable.getAttribute('cmd');
        sendCommandDisableCh(menu, cmd);
    });
    
    btn_ch4_disable.addEventListener("click", (e) => {
        menu = btn_ch4_disable.getAttribute('menu');
        cmd = btn_ch4_disable.getAttribute('cmd');
        sendCommandDisableCh(menu, cmd);
    });

    function sendCommandDisableCh(menu, cmd){
        let url = "http://localhost:8000/control/disable_okuma/";
        let params = "&menu=" + menu + "&cmd=" + cmd;
        console.log('send command');
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }
    
    
});


function disable_ch(dataWs) {

    console.log(dataWs.plc_sensors[".CH1_DISABLE"],dataWs.plc_sensors[".CH2_DISABLE"],dataWs.plc_sensors[".CH3_DISABLE"],dataWs.plc_sensors[".CH4_DISABLE"],dataWs.plc_sensors[".MA1_DISABLE"]);

    //BLOQUES DE HABILITACION PARA OKUMAS
    const cuadrado_mesa1 = document.getElementById("cuadrado_mesa1")
    const cuadrado_mesa2 = document.getElementById("cuadrado_mesa2")
    const cuadrado_okuma1 = document.getElementById("cuadrado_okuma1")
    const cuadrado_okuma2 = document.getElementById("cuadrado_okuma2")
    const cuadrado_okuma3 = document.getElementById("cuadrado_okuma3")
    const cuadrado_okuma4 = document.getElementById("cuadrado_okuma4")

    dataWs.plc_sensors[".MA1_DISABLE"]
    ? (cuadrado_mesa1.className = "cuadrado_mesa1 cuadrado_red")
    : (cuadrado_mesa1.className = "cuadrado_mesa1 cuadrado_green")

    // dataWs.mesa_armado_2 == 1
    // ? (cuadrado_mesa2.className = "cuadrado_mesa2 cuadrado_green")
    // : (cuadrado_mesa2.className = "cuadrado_mesa2 cuadrado_red")

    dataWs.plc_sensors[".CH1_DISABLE"]
    ? (cuadrado_okuma1.className = "cuadrado_okuma1 cuadrado_red")
    : (cuadrado_okuma1.className = "cuadrado_okuma1 cuadrado_green")
    
    dataWs.plc_sensors[".CH2_DISABLE"]
    ? (cuadrado_okuma2.className = "cuadrado_okuma2 cuadrado_red")
    : (cuadrado_okuma2.className = "cuadrado_okuma2 cuadrado_green")

    dataWs.plc_sensors[".CH3_DISABLE"]
    ? (cuadrado_okuma3.className = "cuadrado_okuma3 cuadrado_red")
    : (cuadrado_okuma3.className = "cuadrado_okuma3 cuadrado_green")

    dataWs.plc_sensors[".CH4_DISABLE"]
    ? (cuadrado_okuma4.className = "cuadrado_okuma4 cuadrado_red")
    : (cuadrado_okuma4.className = "cuadrado_okuma4 cuadrado_green")


}