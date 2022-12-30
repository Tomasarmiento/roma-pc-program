window.addEventListener("DOMContentLoaded", () => {
const btn_comenzar = document.getElementById("comenzar")
const btn_detener = document.getElementById("detener")
const btn_terminar = document.getElementById("terminar")
const reset_program = document.getElementById("reset_program")
const btn_terminarOn = document.getElementById("terminarOn")
const btn_terminarOff = document.getElementById("terminarOff")
const btn_paso_paso = document.getElementById("buton_step")

//envio de comandos al tocar botones
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
    const componentemonitorLastAuto = document.getElementById("componentemonitorLastAuto")
    let btns = document.getElementsByTagName('button');


    //invalida botones si no esta en automatico
    for (let i = 1; i <= 6;i++){
        if (dataWs.plc_sensors["R_O_AUT_SEM"] == true) {
            btns[i].disabled = true;
        } else {
            btns[i].disabled = false;
        }
    }

    //muestra leds de okuma seleccionado
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


    //invalida boton si esta en pausa y prende o apaga leds
    var flag = 1
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

    //cambia color ultima vuelta
    if (dataWs.plc_sensors[".last_auto"] == true){
        componentemonitorLastAuto.className = "col-md-12 card card-programa-active text-info mt-3 col-12  shadow rounded componentemonitorLastAuto"
    }
    else {
        componentemonitorLastAuto.className = "col-md-12 card card-programa text-info mt-3 col-12  shadow rounded componentemonitorLastAuto"
    }

    //cambio de color y seguimiento en pasos
    if (document.getElementById("contenedorEstadistica")) {
        var c = document.querySelectorAll("tbody tr")
        if (dataWs.plc_int_variables[".step_auto"] != 0) {
            if (c) {
                //despinta todos los pasos
                for (let i = 1; i <= c.length;i++){
                    step = document.getElementById("step-"+i)
                    step.style.backgroundColor = ""
                }
                step = document.getElementById("step-"+dataWs.plc_int_variables[".step_auto"])
                stepComponent = document.getElementById("componentemonitorStepAuto")

                //scroll para los pasos
                if (dataWs.plc_sensors[".pause_auto"] == false) {
                    if (dataWs.plc_int_variables[".step_auto"] != 1) {
                        var elm = document.getElementById("step-"+(dataWs.plc_int_variables[".step_auto"]-1));
                        elm.scrollIntoView(true);
                    }
                }

                //color de los pasos y monitor
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
