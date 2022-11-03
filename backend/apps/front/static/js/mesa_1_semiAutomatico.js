
window.addEventListener("DOMContentLoaded", () => {
   (window.location.hash);
   //BOTONES
   const btn_move_table1 = document.querySelector("#move_table_1")
   //TEXTOS QUE CAMBIAN RUTINA MESA
   const text_model_selected_mesa = document.querySelector("#text_model_selected_mesa")
   const text_gripper_mesa = document.querySelector("#text_gripper_mesa")
   const text_pos_mesa = document.querySelector("#text_position_mesa")
   const text_take_put_mesa = document.querySelector("#text_take_put_mesa")
   //TEXTOS QUE CAMBIAN RUTINA OKUMA
   const text_model_selected_okuma = document.querySelector("#text_model_selected_okuma")
   const text_gripper_okuma = document.querySelector("#text_gripper_okuma")
   const text_pos_okuma = document.querySelector("#text_position_okuma")
   const text_take_put_okuma = document.querySelector("#text_take_put_okuma")
   const text_pallet_okuma = document.querySelector("#text_pallet_okuma")
   //VALOR DE LOS SELECT
   const model_value = document.getElementById('modelSelect')
   const gripper_value = document.getElementById('gripperSelect')
   const pos_UpDownSelect = document.querySelector('#pos_UpDownSelect')
   const pos_value = document.querySelector('#pos_Select')
   const take_put_value = document.querySelector('#take_putSelect')
   const pos_casita_value = document.querySelector('#pos_casitaSelect')
   const pos_pallet_value = document.querySelector('#pos_palletSelect')
   //VARIABLES PARA ACTUALIZAR LOS MODELOS SELECCIONADOS LOCALES
   var current_pos_casita_value = ""
   var current_take_put_value = ""
   //CONTENEDOR DE LOS VALORES QUE CAMBIAN DEPENDIENDO DE LA RUTINA
   const pallet_selected_container = document.querySelector('#text_pallet_selected')
   //BOTON PARA ENVIAR COMANDO DE EJECUTAR RUTINA
   const btn_semiauto = document.getElementById('btn_semiauto_routine')
   //BOTON PARA ENVIAR COMANDO DE DETENER RUTINA
   const btn_semiauto_stop = document.getElementById('btn_semiauto_routine_stop')
   


    model_value.addEventListener("change", () =>{
        //selector de modelo, habilida selectores dependiendo el modelo
        if (model_value.value == "Mesa_1" || model_value.value == "Mesa_2") {
            disableTxt("pos_casitaSelect",true)
            // disableTxt("pos_palletSelect",true)
            disableTxt("pos_Select",false)
            disableTxt("pos_UpDownSelect",false)
            disableTxt("take_putSelect",false)
            // document.getElementById("text_pallet_selected").style.visibility = "hidden"
            // disableDiv("text_pallet_selected")
            // current_pos_casita_value = ""
            // current_take_put_value = ""
        }
        else{
            disableTxt("pos_casitaSelect",false)
            disableTxt("take_putSelect",false)
            // disableTxt("pos_palletSelect",false)
            disableTxt("pos_Select",true)
            disableTxt("pos_UpDownSelect",true)
            // document.getElementById("text_pallet_selected").style.visibility = "visible"
            current_pos_casita_value = ""
            current_take_put_value = ""
        }
    });

    //reemplaza valores texto para seleccionar el modelo que habilita funciones
    model_value.addEventListener('change', function() {
        // model_value_string = (model_value.value).toString()

        // //inabilita selectores cuando se cambia de modelo
        // if (model_value.value == "Mesa_1" || model_value.value == "Mesa_2") {
        //     disableTxt("pos_casitaSelect",true)
        //     disableTxt("pos_palletSelect",true)
        //     text_model_selected_mesa.innerHTML = model_value_string

        //     //reestablece los valores del mensaje de rutina
        //     text_model_selected_okuma.innerHTML = "______"
        //     text_gripper_okuma.innerHTML = "______"
        //     text_pos_okuma.innerHTML = "______"
        //     text_take_put_okuma.innerHTML = "______"
        //     text_pallet_okuma.innerHTML = "______"
        // }
        // else{
        //     disableTxt("posSelect",true)
        //     text_model_selected_okuma.innerHTML = model_value_string

        //     //reestablece los valores del mensaje de rutina
        //     text_model_selected_mesa.innerHTML = "______"
        //     text_gripper_mesa.innerHTML = "______"
        //     text_pos_mesa.innerHTML = "______"
        //     text_take_put_mesa.innerHTML = "______"
        // }


        // //reestablece valores de los select
        // pos_value.value = "Posición"
        // take_put_value.value = "Tomar/Dejar"
        // pos_casita_value.value = "Posición Casita"
        // pos_pallet_value.value = "Pallet"

        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)

    });

    pos_UpDownSelect.addEventListener('change', function() {
        // position_value_string = (pos_value.value).toString()
        // text_pos_mesa.innerHTML = position_value_string
        // text_gripper_mesa.innerHTML = "Gripper 1" // pone como valor gripper 1 al seleccionar posicion de mesa xq siempre toma o deja con gripper 1

        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)

    });

    pos_value.addEventListener('change', function() {
        // position_value_string = (pos_value.value).toString()
        // text_pos_mesa.innerHTML = position_value_string
        // text_gripper_mesa.innerHTML = "Gripper 1" // pone como valor gripper 1 al seleccionar posicion de mesa xq siempre toma o deja con gripper 1

        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)

    });


    

    take_put_value.addEventListener('change', function() {
        // take_put_value_string = (take_put_value.value).toString()
        
        // if (model_value.value == "Mesa_1" || model_value.value == "Mesa_2") {
        //     text_model_selected_mesa.innerHTML = model_value_string
        //     text_take_put_mesa.innerHTML = take_put_value_string
        // }
        // else{
        //     text_model_selected_okuma.innerHTML = model_value_string
        //     text_take_put_okuma.innerHTML = take_put_value_string
        // }


        // //actualiza el estado actual en una variable local
        // current_take_put_value = take_put_value_string

        // //modifica el texto de gripper dependiendo de que se va a hacer
        // if ((current_take_put_value == "Tomar") && (current_pos_casita_value == "OP 30")) {
        //     text_gripper_okuma.innerHTML = "Gripper 2"
        // } 
        // else if (current_take_put_value == "Dejar" && current_pos_casita_value == "OP 30") {
        //     text_gripper_okuma.innerHTML = "Gripper 1"
        // }
        // else if (current_take_put_value == "Tomar" && current_pos_casita_value == "OP 40"){
        //     text_gripper_okuma.innerHTML = "Gripper 1"
        // }
        // else if (current_take_put_value == "Dejar" && current_pos_casita_value == "OP 40"){
        //     text_gripper_okuma.innerHTML = "Gripper 2"
        // }


        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)
    });

    pos_casita_value.addEventListener('change', function() {
        // // console.log(pos_casita_value.value);
        // position_value_string = (pos_casita_value.value).toString()
        // text_pos_okuma.innerHTML = position_value_string
        // //actualiza el estado actual en una variable local
        // current_pos_casita_value = position_value_string
        // //modifica el texto de gripper dependiendo de que se va a hacer        
        // if (current_take_put_value == "Tomar" && current_pos_casita_value == "OP 30") {
        //     text_gripper_okuma.innerHTML = "Gripper 2"
        // } 
        // else if (current_take_put_value == "Dejar" && current_pos_casita_value == "OP 30") {
        //     text_gripper_okuma.innerHTML = "Gripper 1"
        // }
        // else if (current_take_put_value == "Tomar" && current_pos_casita_value == "OP 40"){
        //     text_gripper_okuma.innerHTML = "Gripper 1"
        // }
        // else if (current_take_put_value == "Dejar" && current_pos_casita_value == "OP 40"){
        //     text_gripper_okuma.innerHTML = "Gripper 2"
        // }

        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)
    });

    // pos_pallet_value.addEventListener('change', function() {
    //     // pallet_value_string = (pos_pallet_value.value).toString()
    //     // text_pallet_okuma.innerHTML = pallet_value_string

    //     //manda comando al back con lo seleccionado y el menu para rutina de semiautomatico
    //     const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
    //     console.log(name_bit);
    //     sendCommandSemi("semi", name_bit)

    // });

    btn_semiauto.addEventListener('click', (e) => {
        sendCommandSemi("semi","execute_routine")
        console.log(model_value.value,current_take_put_value);

    });

    btn_semiauto_stop.addEventListener('click', (e) => {
        sendCommandSemi("semi","stop_routine")
    });
    

    // console.log('hola',conectionWs());
    


    // socket.onmessage = function (event) {
    //     const datosWs2 = JSON.parse(event.data);
    //     console.log(datosWs2);
    //     // console.log('dentro de socket message');
    // };


    
    

    
    
    function sendCommandSemi(menu, name_bit){
        let url = "http://localhost:8000/control/semiautomatico/routine/";
        let params = "&menu=" + menu + "&name=" + name_bit;
        console.log('send command');
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }

    
});

function semiAutomatico(dataWs) {
    //CONTENEDORES DE LAS RUTINAS
    const routine_container_okuma = document.querySelector("#routine_container_okuma")
    const routine_container_mesa = document.querySelector("#routine_container_mesa")



    //TEXTOS QUE CAMBIAN RUTINA MESA
    const text_model_selected_mesa = document.querySelector("#text_model_selected_mesa")
    const text_gripper_mesa = document.querySelector("#text_gripper_mesa")
    const text_pos_up_down_mesa = document.querySelector("#text_position_up_down_mesa")
    const text_pos_mesa = document.querySelector("#text_position_mesa")
    const text_take_put_mesa = document.querySelector("#text_take_put_mesa")
    //TEXTOS QUE CAMBIAN RUTINA OKUMA
    const text_model_selected_okuma = document.querySelector("#text_model_selected_okuma")
    const text_gripper_okuma = document.querySelector("#text_gripper_okuma")
    const text_pos_okuma = document.querySelector("#text_position_okuma")
    const text_take_put_okuma = document.querySelector("#text_take_put_okuma")
    const text_pallet_okuma = document.querySelector("#text_pallet_okuma")
    
    // console.log(dataWs.plc_sensors.R_I_MA_CH);
    if (dataWs.plc_sensors.R_I_MA_CH == true) {
        routine_container_mesa.className = "sub_routine_container_class block_sub_routine_container_class"
        routine_container_okuma.className = "sub_routine_container_class"
        text_model_selected_mesa.innerHTML = "______"
        text_pos_up_down_mesa.innerHTML = "______"
        text_gripper_mesa.innerHTML = "______"
        text_pos_mesa.innerHTML = "______"
        text_take_put_mesa.innerHTML = "______"
        
    } 
    else{
        routine_container_okuma.className = "sub_routine_container_class block_sub_routine_container_class"
        routine_container_mesa.className = "sub_routine_container_class"
        //reestablece los valores del mensaje de rutina
        text_model_selected_okuma.innerHTML = "______"
        text_gripper_okuma.innerHTML = "______"
        text_pos_okuma.innerHTML = "______"
        text_take_put_okuma.innerHTML = "______"
        text_pallet_okuma.innerHTML = "______"
        
    }

    //SI ES MESA
    if (dataWs.plc_sensors.R_I_MA_CH == false) {
        text_gripper_mesa.innerHTML = "GRIPPER 1"
        //SI ES MESA1 O MESA 2
        if (dataWs.plc_sensors.R_I_MA == true) {
            text_model_selected_mesa.innerHTML = "MESA 2"
        }
        else{
            text_model_selected_mesa.innerHTML = "MESA 1"
        }
        //TOMAR_DEJAR
        if (dataWs.plc_sensors.R_I_GET_PUT == true) {
            text_take_put_mesa.innerHTML = "DEJAR"
        }
        else{
            text_take_put_mesa.innerHTML = "TOMAR"
        }
        //SI ES ARRIBA O ABAJO
        if (dataWs.plc_sensors.R_I_DRW == true) {
            text_pos_up_down_mesa.innerHTML = "ARRIBA"
        }
        else{
            text_pos_up_down_mesa.innerHTML = "ABAJO"
        }
        //SI ES POS 1 O 2
        if (dataWs.plc_sensors.R_I_PAL == true) {
            text_pos_mesa.innerHTML = "&nbsp 2"
        }
        else{
            text_pos_mesa.innerHTML = "&nbsp 1"
        }
    }

    //SI ES OKUMA
    else{
        //SI ES OKUMA 1,2,3,4
        if (dataWs.plc_sensors.R_I_BIT0_CH == false && dataWs.plc_sensors.R_I_BIT1_CH == false) {
            text_model_selected_okuma.innerHTML = "OKUMA 1"
        }
        else if (dataWs.plc_sensors.R_I_BIT0_CH == false && dataWs.plc_sensors.R_I_BIT1_CH == true) {
            text_model_selected_okuma.innerHTML = "OKUMA 3"
        }
        else if (dataWs.plc_sensors.R_I_BIT0_CH == true && dataWs.plc_sensors.R_I_BIT1_CH == false) {
            text_model_selected_okuma.innerHTML = "OKUMA 2"
        }
        else{
            text_model_selected_okuma.innerHTML = "OKUMA 4"
        }
        //TOMAR_DEJAR
        if (dataWs.plc_sensors.R_I_GET_PUT == true) {
            text_take_put_okuma.innerHTML = "DEJAR"
        }
        else{
            text_take_put_okuma.innerHTML = "TOMAR"
        }
        //SI ES GRIPPER 1 O GRIPPER 2
        if (dataWs.plc_sensors.R_I_GET_PUT == false && dataWs.plc_sensors.R_I_30_40 == false) {
            text_gripper_okuma.innerHTML = "GRIPPER 2"
        }
        else if(dataWs.plc_sensors.R_I_GET_PUT == true && dataWs.plc_sensors.R_I_30_40 == false) {
            text_gripper_okuma.innerHTML = "GRIPPER 1"
        }
        else if(dataWs.plc_sensors.R_I_GET_PUT == false && dataWs.plc_sensors.R_I_30_40 == true) {
            text_gripper_okuma.innerHTML = "GRIPPER 1"
        }
        else{
            text_gripper_okuma.innerHTML = "GRIPPER 2"
        }
        //SI ES OP30 U OP40
        if (dataWs.plc_sensors.R_I_30_40 == true) {
            text_pos_okuma.innerHTML = "OP 40"
        }
        else{
            text_pos_okuma.innerHTML = "OP 30"
        }
        //SI ES PALLET 1 O PALLET 2
        if (dataWs.plc_sensors.R_I_CAS == true) {
            text_pallet_okuma.innerHTML = "PALLET 2"
        }
        else{
            text_pallet_okuma.innerHTML = "PALLET 1"
        }

    }
    
}