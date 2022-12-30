
window.addEventListener("DOMContentLoaded", () => {
   (window.location.hash);
   //VALOR DE LOS SELECT
   const model_value = document.getElementById('modelSelect')
   const gripper_value = document.getElementById('gripperSelect')
   const pos_UpDownSelect = document.querySelector('#pos_UpDownSelect')
   const pos_value = document.querySelector('#pos_Select')
   const take_put_value = document.querySelector('#take_putSelect')
   const pos_casita_value = document.querySelector('#pos_casitaSelect')
   //VARIABLES PARA ACTUALIZAR LOS MODELOS SELECCIONADOS LOCALES
   var current_pos_casita_value = ""
   var current_take_put_value = ""
   //BOTON PARA ENVIAR COMANDO DE EJECUTAR RUTINA
   const btn_semiauto_start = document.getElementById('btn_semiauto_routine')
   //BOTON PARA ENVIAR COMANDO DE DETENER RUTINA
   const btn_semiauto_stop = document.getElementById('btn_semiauto_routine_stop')
   const btn_reset_program = document.getElementById('btn_semiauto_reset_program')
   const btn_step = document.getElementById('btn_semiauto_step')
   const btn_run_program = document.getElementById('btn_semiauto_ejecutar')
   


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
            current_pos_casita_value = ""
            current_take_put_value = ""
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
        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)

    });

    pos_UpDownSelect.addEventListener('change', function() {
        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)

    });

    pos_value.addEventListener('change', function() {
        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)

    });

    take_put_value.addEventListener('change', function() {
        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)
    });

    pos_casita_value.addEventListener('change', function() {
        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)
    });


    //manda comandos cuando se aprieta boton
    btn_semiauto_start.addEventListener("click", (e) => {
        menu = btn_semiauto_start.getAttribute('menu');
        cmd = btn_semiauto_start.getAttribute('cmd');
        sendCommandSemiButton(menu, cmd);
    });

    btn_semiauto_stop.addEventListener("click", (e) => {
        menu = btn_semiauto_stop.getAttribute('menu');
        cmd = btn_semiauto_stop.getAttribute('cmd');
        sendCommandSemiButton(menu, cmd);
    });

    btn_reset_program.addEventListener("click", (e) => {
        menu = btn_reset_program.getAttribute('menu');
        cmd = btn_reset_program.getAttribute('cmd');
        sendCommandSemiButton(menu, cmd);
    });

    btn_step.addEventListener("click", (e) => {
        menu = btn_step.getAttribute('menu');
        cmd = btn_step.getAttribute('cmd');
        sendCommandSemiButton(menu, cmd);
    });
    
    btn_run_program.addEventListener("click", (e) => {
        menu = btn_run_program.getAttribute('menu');
        cmd = btn_run_program.getAttribute('cmd');
        sendCommandSemiButton(menu, cmd);
    });

  
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


    function sendCommandSemiButton(menu, cmd){
        let url = "http://localhost:8000/control/semiautomatico/routine/";
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



    //invalida botones si no esta en semiautomatico
    let btns = document.getElementsByTagName('button');
    for (let i = 1; i <= btns.length-1;i++){
        if (dataWs.plc_sensors["R_O_AUT_SEM"] == false) {
            btns[i].disabled = true
        } else {
            btns[i].disabled = false;
        }
    
    }

    //activa botones si esta en pausa y semi
    var flag = 1
    if (dataWs.plc_sensors[".pause_semi"] == true && dataWs.plc_sensors["R_O_AUT_SEM"] == true){
        if (flag == 1) {
            document.getElementById("btn_semiauto_reset_program").disabled = false;
            document.getElementById("btn_semiauto_step").disabled = false;
            flag ++
        }
    }
    else {
        document.getElementById("btn_semiauto_reset_program").disabled = true;
        document.getElementById("btn_semiauto_step").disabled = true;
    }


    //interacciones con el monitor
    if (document.getElementById("contenedorEstadistica")) {
        var a = document.getElementById("contenedorEstadistica")
        var c = a.querySelectorAll("tbody tr")
        if (dataWs.plc_int_variables[".step_semi"] != 0) {
            if (c) {
                //despinta todos los pasos
                for (let i = 1; i <= c.length;i++){
                    step = document.getElementById("step-"+i)
                    if (step) {
                        step.style.backgroundColor = ""
                    }
                }
                step = document.getElementById("step-"+dataWs.plc_int_variables[".step_semi"])
                stepComponent = document.getElementById("componentemonitorSemi")

                //scroll a los pasos
                if (dataWs.plc_sensors[".pause_semi"] == false) {
                    if (dataWs.plc_int_variables[".step_semi"] != 1) {
                        var elm = document.getElementById("step-"+(dataWs.plc_int_variables[".step_semi"]-1));
                        elm.scrollIntoView(true);
                    }
                }
                //cambia color de pasos
                if (dataWs.plc_sensors[".init_error"] == true) {
                    step.style.backgroundColor = "red"
                    stepComponent.style.borderColor = "red"
                } else {
                    if (dataWs.plc_sensors[".pause_semi"] == true) {
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
    
    //inhabilita y reestablece los selectores dependiendo que se elecciona
    if (dataWs.plc_sensors.R_I_MA_CH == true) {
        routine_container_mesa.className = "sub_routine_container_class block_sub_routine_container_class"
        routine_container_okuma.className = "sub_routine_container_class"
        //reestablece los valores del mensaje de rutina
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