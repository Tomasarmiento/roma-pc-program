window.addEventListener("DOMContentLoaded", () => {
const btn_comenzar = document.getElementById("comenzar")
const btn_detener = document.getElementById("detener")
const btn_terminar = document.getElementById("terminar")
const reset_program = document.getElementById("reset_program")
const btn_terminarOn = document.getElementById("terminarOn")
const btn_terminarOff = document.getElementById("terminarOff")
const btn_paso_paso = document.getElementById("buton_step")


reset_program.addEventListener("click", (e) => {
    menu = reset_program.getAttribute('menu');
    cmd = reset_program.getAttribute('cmd');
    sendCommandAuto(menu, cmd);
});

btn_terminarOn.addEventListener("click", (e) => {
    menu = btn_terminarOn.getAttribute('menu');
    cmd = btn_terminarOn.getAttribute('cmd');
    sendCommandAuto(menu, cmd);
});

btn_terminarOff.addEventListener("click", (e) => {
    menu = btn_terminarOff.getAttribute('menu');
    cmd = btn_terminarOff.getAttribute('cmd');
    sendCommandAuto(menu, cmd);
});

btn_detener.addEventListener("click", (e) => {
    menu = btn_detener.getAttribute('menu');
    cmd = btn_detener.getAttribute('cmd');
    sendCommandAuto(menu, cmd);
});


btn_comenzar.addEventListener("click", (e) => {
    menu = btn_comenzar.getAttribute('menu');
    cmd = btn_comenzar.getAttribute('cmd');
    sendCommandAuto(menu, cmd);
});

btn_paso_paso.addEventListener("click", (e) => {
    menu = btn_paso_paso.getAttribute('menu');
    cmd = btn_paso_paso.getAttribute('cmd');
    sendCommandAuto(menu, cmd);
});



function sendCommandAuto(menu, cmd){
    let url = "http://localhost:8000/control/automatico/buttons-cmd/";
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

function auto_step(dataWs) {
    // automatic_leds = ["led-comenzar","led-detener","led-terminar","led-reset-program"]
    const led_comenzar = document.getElementById("led-comenzar")
    const led_detener = document.getElementById("led-detener")
    const led_terminar = document.getElementById("led-terminar")
    const led_reset_program = document.getElementById("led-reset-program")
    const hash_manual = document.getElementById("manual_hash")

    if (dataWs.plc_sensors["R_O_AUT_SEM"] == true) {
        document.body.style.backgroundColor = "grey"
        
    } else {
        document.body.style.backgroundColor = "green"
    }


    // console.log(dataWs.plc_sensors[".pause_auto"]);
    var flag = 1
    //invalida boton si esta en pausa y prende o apaga leds
    if (dataWs.plc_sensors[".pause_auto"] == true){
        led_detener.className = "led led-red mb-5";
        led_comenzar.className = "led led-grey mb-5";
        if (flag == 1) {
            document.getElementById("reset_program").disabled = false;
            document.getElementById("buton_step").disabled = false;
            flag ++
        }
    }
    else {
        led_detener.className = "led led-grey mb-5";
        led_comenzar.className = "led led-green mb-5";
        document.getElementById("reset_program").disabled = true;
        document.getElementById("buton_step").disabled = true;
    }


    if (dataWs.plc_sensors[".last_auto"] == true){
        led_terminar.className = "led led-green mb-5";
    }
    else {
        led_terminar.className = "led led-grey mb-5";
    }

    // console.log(dataWs.plc_sensors[".step_auto"]);
    if (document.getElementById("contenedorEstadistica")) {
        // step = document.getElementById("step-"+dataWs.plc_sensors[".step_auto"])
        // console.log(step);
        var c = document.querySelectorAll("tbody tr")
        console.log(c.length);
        if (c) {
            for (let i = 1; i <= c.length;i++){
                step = document.getElementById("step-"+i)
                step.style.backgroundColor = ""
            }
            step = document.getElementById("step-"+dataWs.plc_sensors[".step_auto"])
            // for (let i = 0; i <= dataWs.mensajes_log.length-1;i++){
            //     // console.log(dataWs.mensajes_log[i].length);
            //     if (dataWs.mensajes_log[i].length > 0) {
            //         console.log('es mayorrrr');
            //         step.style.backgroundColor = "red"
            //     } else {
            //         console.log('es menor');
            //     }
            // }
            if (dataWs.plc_sensors[".init_error"] == true) {
                step.style.backgroundColor = "red"
            } else {
                step.style.backgroundColor = "lightgreen"
            }
            
            
            
        }

        

    }

   
}
