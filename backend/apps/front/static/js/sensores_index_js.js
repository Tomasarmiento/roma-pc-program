window.addEventListener("DOMContentLoaded", () => {
    const list_of_tables = ['tablaDrawer1','tablaDrawer2','tablaSensoresCNC1', 'tablaSensoresCNC2','tablaSensoresCNC3','tablaSensoresCNC4']
    //DEPENDIENDO EL HASH LLAMA A LA FUNCION PARA DESABILITAR LA LISTA DE SENSORES DE LOS DEMAS
    if (window.location.pathname == '/mesa_1_neumatic/') {
        disableDivExeptValue('tablaDrawer1',list_of_tables)
    }
    else if(window.location.pathname == /mesa_2_neumatic/) {
        disableDivExeptValue('tablaDrawer2',list_of_tables)
    }
    else if(window.location.pathname == /okuma_1_neumatic/) {//tablaSensoresCNC1
        disableDivExeptValue('tablaSensoresCNC1',list_of_tables)
    }
    else if(window.location.pathname == /okuma_2_neumatic/) {//tablaSensoresCNC1
        disableDivExeptValue('tablaSensoresCNC2',list_of_tables)
    }
    else if(window.location.pathname == /okuma_3_neumatic/) {//tablaSensoresCNC1
        disableDivExeptValue('tablaSensoresCNC3',list_of_tables)
    }
    else if(window.location.pathname == /okuma_4_neumatic/) {//tablaSensoresCNC1
        disableDivExeptValue('tablaSensoresCNC4',list_of_tables)
    }
    else if(window.location.pathname == /semiAutomatico/) {//tablaSensoresCNC1
        disableDivExeptValue('',list_of_tables)
    }

    console.log(window.location.pathname);
   
    });
    //sensores states//
function sensores(dataWs) {

    const list_inverted_signal = ['MA1_I_DR_U_PS_1','MA1_I_DR_U_PS_2','MA1_I_DR_D_PS_1','MA1_I_DR_D_PS_2']
    const list_1flag_2leds = ['R_I_AUT_SEM','R_I_30_40','R_I_CAS','R_I_BIT0_CH','R_I_BIT1_CH','R_I_PAL','R_I_DRW','R_I_MA','R_I_GET_PUT','R_I_MA_CH','INF30','Blower','Booster','INF40']
    const list_okuma_selector = ['R_I_BIT0_CH','R_I_BIT1_CH']
    const list_okuma_selector_bit0 = ['R_I_BIT0_CH']
    const list_okuma_selector_bit1 = ['R_I_BIT1_CH']

    var R_I_BIT0_CH = false
    var R_I_BIT1_CH = false

    
    // console.log("atras: ",dataWs.plc_sensors.CH1_I_NPR,"adelante: ",dataWs.plc_sensors.CH1_I_NPA);
    // console.log(dataWs.plc_sensors);
    dict = dataWs.plc_sensors
    arr_of_dict = Object.keys(dict)
    for (sensor_key of arr_of_dict) {
        // console.log(arr_of_dict);
        if (dataWs.plc_sensors[sensor_key] == true){
            //señales invertidas
            if (list_inverted_signal.includes(sensor_key)) {
                see_state_sensor(sensor_key,false)
            }
            //señales comunes
            else {
                see_state_sensor(sensor_key,true)
                see_state_sensor(sensor_key+"_copy",false)
                see_state_sensor(sensor_key+"_1_copy",true)
            }
            //rutinas robot
            if (list_1flag_2leds.includes(sensor_key)) {
                see_state_sensor(sensor_key,false)
                see_state_sensor(sensor_key+"_1",true)
            }
            //okuma selector
            if (list_okuma_selector_bit0.includes(sensor_key)) {
                R_I_BIT0_CH = true
            }
            if (list_okuma_selector_bit1.includes(sensor_key)) {
                R_I_BIT1_CH = true
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
                see_state_sensor(sensor_key+"_1_copy",false)
            }
            //rutinas robot
            if (list_1flag_2leds.includes(sensor_key)) {
                see_state_sensor(sensor_key,true)
                see_state_sensor(sensor_key+"_1",false)
            }
            //okuma selector
            if (list_okuma_selector_bit0.includes(sensor_key)) {
                R_I_BIT0_CH = false
            }
            if (list_okuma_selector_bit1.includes(sensor_key)) {
                R_I_BIT1_CH = false
            }

        }
    }
    // okumas bits
    if (R_I_BIT0_CH == true && R_I_BIT1_CH == false) {
        see_state_sensor('okuma_2',true)
        see_state_sensor('okuma_1',false)
        see_state_sensor('okuma_3',false)
        see_state_sensor('okuma_4',false)
    }
    if (R_I_BIT0_CH == false && R_I_BIT1_CH == true) {
        see_state_sensor('okuma_3',true)
        see_state_sensor('okuma_1',false)
        see_state_sensor('okuma_2',false)
        see_state_sensor('okuma_4',false)
    }
    if (R_I_BIT0_CH == false && R_I_BIT1_CH == false) {
        see_state_sensor('okuma_1',true)
        see_state_sensor('okuma_3',false)
        see_state_sensor('okuma_2',false)
        see_state_sensor('okuma_4',false)
    }
    if (R_I_BIT0_CH == true && R_I_BIT1_CH == true) {
        see_state_sensor('okuma_4',true)
        see_state_sensor('okuma_1',false)
        see_state_sensor('okuma_2',false)
        see_state_sensor('okuma_3',false)
    }
   

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

};