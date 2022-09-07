window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    //sensores states//
    const arrSensores = ["signal_0","signal_1","signal_2","signal_3","signal_4","signal_5","signal_6","signal_7","signal_8","signal_9"]
    function see_state_sensor(sensor_name,state,invest) {
        // console.log(sensor_name);
        const sensor_name_id = document.getElementById( sensor_name );
        // console.log(sensor_name_id);
        if (state == true){
            sensor_name_id.className = "led led-green";
                // if(invest == true){
                //     sensor_name_id.className = "led led-grey";
                // }
                // else{
                //     sensor_name_id.className = "led led-green";
                // }
        }
        else{
            sensor_name_id.className = "led led-grey";
        }

    }
    see_state_sensor("signal_0")
    //sensores states//
    socket.onmessage = function (event) {
        const datosWs = JSON.parse(event.data);
        var variable = "signal_0"
        // console.log(datosWs[variable]);
        for (sensor_key of arrSensores) {
            // console.log(datosWs);
            if (datosWs[sensor_key] == true){
                see_state_sensor(sensor_key,true)
            }
            else{
                see_state_sensor(sensor_key,false)
            }
        }
    };  
});