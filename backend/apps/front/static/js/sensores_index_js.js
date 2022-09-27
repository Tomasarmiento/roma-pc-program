window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    //sensores states//
    const list_of_tables = ['tablaDrawer1','tablaDrawer2','tablaSensoresCNC1', 'tablaSensoresCNC2','tablaSensoresCNC3','tablaSensoresCNC4']
    const list_inverted_signal = ['MA1_I_DR_U_PS_1','MA1_I_DR_U_PS_2','MA1_I_DR_D_PS_1','MA1_I_DR_D_PS_2']


    //DEPENDIENDO EL HASH LLAMA A LA FUNCION PARA DESABILITAR LA LISTA DE SENSORES DE LOS DEMAS
    if (window.location.pathname == '/mesa_1_neumatic/') {
        disableDiv('tablaDrawer1',list_of_tables)
    }
    else if(window.location.pathname == /mesa_2_neumatic/) {
        disableDiv('tablaDrawer2',list_of_tables)
    }
    else if(window.location.pathname == /okuma_1_neumatic/) {//tablaSensoresCNC1
        disableDiv('tablaSensoresCNC1',list_of_tables)
    }
    else if(window.location.pathname == /okuma_2_neumatic/) {//tablaSensoresCNC1
        disableDiv('tablaSensoresCNC2',list_of_tables)
    }
    else if(window.location.pathname == /okuma_3_neumatic/) {//tablaSensoresCNC1
        disableDiv('tablaSensoresCNC3',list_of_tables)
    }
    else if(window.location.pathname == /okuma_4_neumatic/) {//tablaSensoresCNC1
        disableDiv('tablaSensoresCNC4',list_of_tables)
    }

    console.log(window.location.pathname);
    function see_state_sensor(sensor_name,state,invest) {
        // console.log(sensor_name);
        const sensor_name_id = document.getElementById( sensor_name );
        // console.log(sensor_name_id);
        if (sensor_name_id){
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
        else{
            // console.log("No existe un led con ese nombre");
        }


    }
    //sensores states//
    socket.onmessage = function (event) {
        const datosWs = JSON.parse(event.data);
        dict = datosWs.plc_sensors
        arr_of_dict = Object.keys(dict)
        for (sensor_key of arr_of_dict) {
            // console.log(arr_of_dict);
            if (datosWs.plc_sensors[sensor_key] == true){
                if (list_inverted_signal.includes(sensor_key)) {
                    see_state_sensor(sensor_key,false)
                }
                else {
                    see_state_sensor(sensor_key,true)
                }
            }
            else {
                if (list_inverted_signal.includes(sensor_key)) {
                    see_state_sensor(sensor_key,true)
                }
                else{
                    see_state_sensor(sensor_key,false)
                }
            }
        }
    };  
});