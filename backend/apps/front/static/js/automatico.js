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
    console.log(dataWs.plc_sensors.CH1_I_PSA);
    
}
