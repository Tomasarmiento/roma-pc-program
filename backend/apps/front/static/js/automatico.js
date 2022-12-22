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

    // console.log(dataWs.plc_sensors[".init_error"]);
    // automatic_leds = ["led-comenzar","led-detener","led-terminar","led-reset-program"]
    const led_comenzar = document.getElementById("led-comenzar")
    const led_detener = document.getElementById("led-detener")
    const led_terminar = document.getElementById("led-terminar")
    const led_reset_program = document.getElementById("led-reset-program")
    const hash_manual = document.getElementById("manual_hash")
    const componentemonitorLastAuto = document.getElementById("componentemonitorLastAuto")

    // if (dataWs.plc_sensors["R_O_AUT_SEM"] == true) {
    //     document.body.style.backgroundColor = "grey"
        
    // } else {
    //     document.body.style.backgroundColor = "rgb(113, 172, 121)"
    // }
    let btns = document.getElementsByTagName('button');
    for (let i = 1; i <= 6;i++){
        // console.log(btns[i].disabled=false);
        if (dataWs.plc_sensors["R_O_AUT_SEM"] == true) {
            // i.disabled = false;
            // alert("Modo automatico desactivado")
            // alertAuto++
            btns[i].disabled = true;
            
        } else {
            // i.disabled = true;
            btns[i].disabled = false;
        }
    
    }

    
    if (dataWs.plc_sensors["R_I_BIT0_CH"] == true && dataWs.plc_sensors["R_I_BIT1_CH"] == false) {
        see_state_sensor_automatic('okuma_2',true,true)
        see_state_sensor_automatic('okuma_1',false,true)
        see_state_sensor_automatic('okuma_3',false,true)
        see_state_sensor_automatic('okuma_4',false,true)
    }
    if (dataWs.plc_sensors["R_I_BIT0_CH"] == false && dataWs.plc_sensors["R_I_BIT1_CH"] == true) {
        see_state_sensor_automatic('okuma_3',true,true)
        see_state_sensor_automatic('okuma_1',false,true)
        see_state_sensor_automatic('okuma_2',false,true)
        see_state_sensor_automatic('okuma_4',false,true)
    }
    if (dataWs.plc_sensors["R_I_BIT0_CH"] == false && dataWs.plc_sensors["R_I_BIT1_CH"] == false) {
        see_state_sensor_automatic('okuma_1',true,true)
        see_state_sensor_automatic('okuma_3',false,true)
        see_state_sensor_automatic('okuma_2',false,true)
        see_state_sensor_automatic('okuma_4',false,true)
    }
    if (dataWs.plc_sensors["R_I_BIT0_CH"] == true && dataWs.plc_sensors["R_I_BIT1_CH"] == true) {
        see_state_sensor_automatic('okuma_4',true,true)
        see_state_sensor_automatic('okuma_1',false,true)
        see_state_sensor_automatic('okuma_2',false,true)
        see_state_sensor_automatic('okuma_3',false,true)
    }


    var flag = 1
    //invalida boton si esta en pausa y prende o apaga leds
    if (dataWs.plc_sensors[".pause_auto"] == true){
        if (flag == 1) {
            document.getElementById("reset_program").disabled = false;
            document.getElementById("buton_step").disabled = false;
            flag ++
        }
    }
    else {
        document.getElementById("reset_program").disabled = true;
        document.getElementById("buton_step").disabled = true;
    }

    if (dataWs.plc_sensors[".last_auto"] == true){
        componentemonitorLastAuto.className = "col-md-12 card card-programa-active text-info mt-3 col-12  shadow rounded componentemonitorLastAuto"
    }
    else {
        componentemonitorLastAuto.className = "col-md-12 card card-programa text-info mt-3 col-12  shadow rounded componentemonitorLastAuto"
    }

    if (document.getElementById("contenedorEstadistica")) {
        var c = document.querySelectorAll("tbody tr")
        if (dataWs.plc_int_variables[".step_auto"] != 0) {
            if (c) {
                for (let i = 1; i <= c.length;i++){
                    step = document.getElementById("step-"+i)
                    step.style.backgroundColor = ""
                }
                step = document.getElementById("step-"+dataWs.plc_int_variables[".step_auto"])
                stepComponent = document.getElementById("componentemonitorStepAuto")

                //pedido de paso
                if (dataWs.plc_sensors[".pause_auto"] == false) {
                    if (dataWs.plc_int_variables[".step_auto"] != 1) {
                        var elm = document.getElementById("step-"+(dataWs.plc_int_variables[".step_auto"]-1));
                        elm.scrollIntoView(true);
                    }
                }
                //pedido de paso


                // for (let i = 0; i <= dataWs.mensajes_log.length-1;i++){
                //     // console.log(dataWs.mensajes_log[i].length);
                //     if (dataWs.mensajes_log[i].length > 0) {
                //         step.style.backgroundColor = "red"
                //     } else {
                //     }
                // }
                // dataWs.plc_sensors[".init_error"] = false
                // dataWs.plc_sensors[".pause_auto"] = false
                // console.log(dataWs.plc_sensors[".init_error"]);
                if (dataWs.plc_sensors[".init_error"] == true) {
                    step.style.backgroundColor = "red"
                    stepComponent.style.borderColor = "red"
                } else {
                    if (dataWs.plc_sensors[".pause_auto"] == true) {
                        step.style.backgroundColor = "rgb(255, 238, 0)"
                        stepComponent.style.borderColor = "rgb(255, 238, 0)"
                    }
                    else{
                        step.style.backgroundColor = "lightgreen"
                        stepComponent.style.borderColor = "lightgreen"
                    }
                    
                }
            }
        }
    }
}
