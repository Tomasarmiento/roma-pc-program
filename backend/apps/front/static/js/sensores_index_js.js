window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    //sensores states//
    const list_of_tables = ['tablaDrawer1','tablaDrawer2','tablaSensoresCNC1', 'tablaSensoresCNC2','tablaSensoresCNC3','tablaSensoresCNC4']
    const list_inverted_signal = ['MA1_I_DR_U_PS_1','MA1_I_DR_U_PS_2','MA1_I_DR_D_PS_1','MA1_I_DR_D_PS_2']
    const list_robot_routines_signal = ['R_I_AUT_SEM','R_I_30_40','R_I_CAS','R_I_BIT0_CH','R_I_BIT1_CH','R_I_PAL','R_I_DRW','R_I_MA','R_I_GET_PUT','R_I_MA_CH']
    const list_okuma_selector = ['R_I_BIT0_CH','R_I_BIT1_CH']

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
        const sensor_name_id = document.getElementById( sensor_name );
        if (sensor_name_id){
            if (state == true){
                sensor_name_id.className = "led led-green";
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
        var count = 0
        const datosWs = JSON.parse(event.data);
        dict = datosWs.plc_sensors
        arr_of_dict = Object.keys(dict)
        for (sensor_key of arr_of_dict) {
            // console.log(arr_of_dict[0]+"1");
            if (datosWs.plc_sensors[sensor_key] == true){
                //señales invertidas
                if (list_inverted_signal.includes(sensor_key)) {
                    see_state_sensor(sensor_key,false)
                }
                //señales comunes
                else {
                    see_state_sensor(sensor_key,true)
                    see_state_sensor(sensor_key+"_copy",false)
                }
                //rutinas robot
                if (list_robot_routines_signal.includes(sensor_key)) {
                    see_state_sensor(sensor_key,false)
                    see_state_sensor(sensor_key+"_1",true)
                }
                //okuma selector
                if (list_okuma_selector.includes(sensor_key)) {
                    console.log(sensor_key);
                    count = count + 1
                    if (count == 2){
                        see_state_sensor("okuma_1",true)
                    }
                        // see_state_sensor(sensor_key,false)
                        // see_state_sensor(sensor_key+"_1",true)
                }

            }
            else {
                //señales invertidas
                if (list_inverted_signal.includes(sensor_key)) {
                    see_state_sensor(sensor_key,true)
                }
                //señales comunes
                else{
                    see_state_sensor(sensor_key,false)
                    see_state_sensor(sensor_key+"_copy",true)
                }
                //rutinas robot
                if (list_robot_routines_signal.includes(sensor_key)) {
                    see_state_sensor(sensor_key,true)
                    see_state_sensor(sensor_key+"_1",false)
                }
                if (list_okuma_selector.includes(sensor_key)) {
                    count = count + 1
                    if (count == 2){
                        see_state_sensor("okuma_4",true)
                    }
                    console.log(count);
                        // see_state_sensor(sensor_key,false)
                        // see_state_sensor(sensor_key+"_1",true)
                }
            }
        }
    };  
});