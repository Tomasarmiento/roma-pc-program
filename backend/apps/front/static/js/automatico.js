window.addEventListener("DOMContentLoaded", () => {
const btn_comenzar = document.getElementById("comenzar")
const btn_detener = document.getElementById("detener")
const btn_terminar = document.getElementById("terminar")
const reset_program = document.getElementById("reset_program")


reset_program.addEventListener("click", (e) => {
    menu = reset_program.getAttribute('menu');
    cmd = reset_program.getAttribute('cmd');
    sendCommandAuto(menu, cmd);
});

btn_terminar.addEventListener("click", (e) => {
    menu = btn_terminar.getAttribute('menu');
    cmd = btn_terminar.getAttribute('cmd');
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

    console.log(dataWs.plc_sensors[".pause_auto"]);
    var flag = 1
    if (dataWs.plc_sensors[".pause_auto"] == true){
        led_detener.className = "led led-red mb-5";
        led_comenzar.className = "led led-grey mb-5";
        // see_state_sensor("led-detener",true)
        // see_state_sensor("led-comenzar",false)
        if (flag == 1) {
            document.getElementById("reset_program").disabled = false;
            flag ++    
        }
    }
    else {
        led_detener.className = "led led-grey mb-5";
        led_comenzar.className = "led led-green mb-5";
        document.getElementById("reset_program").disabled = true;
        // see_state_sensor("led-comenzar",true)
        // see_state_sensor("led-detener",false)
    }


    // for (automatic_led of automatic_led) {
    //     if (dataWs.plc_sensors[sensor_key] == true){

    //     }

    // }
    


    // console.log(flag);
    
}
