window.addEventListener("DOMContentLoaded", () => {
   (window.location.hash);
   //BOTONES
   const btn_move_table1 = document.querySelector("#move_table_1")
   //TEXTOS QUE CAMBIAN EN RUTINA
   const text_model_selected = document.querySelector("#text_model_selected")
   //TEXTOS QUE CAMBIAN EN SUB RUTINA MESAS
   const text_gripper = document.querySelector("#text_gripper")
   const text_pos = document.querySelector("#text_position")
   const text_take_put = document.querySelector("#text_take_put")
   const text_pallet = document.querySelector("#text_pallet")
   //VALOR DE LOS SELECT
   const model_value = document.getElementById('modelSelect')
   const gripper_value = document.getElementById('gripperSelect')
   const pos_value = document.querySelector('#posSelect')
   const take_put_value = document.querySelector('#take_putSelect')
   const pos_casita_value = document.querySelector('#pos_casitaSelect')
   const pos_pallet_value = document.querySelector('#pos_palletSelect')
   //VARIABLES PARA ACTUALIZAR LOS MODELOS SELECCIONADOS LOCALES
   var current_pos_casita_value = ""
   var current_take_put_value = ""
   //CONTENEDOR DE LOS VALORES QUE CAMBIAN DEPENDIENDO DE LA RUTINA
   const pallet_selected_container = document.querySelector('#text_pallet_selected')



    model_value.addEventListener("change", () =>{
        //selector de modelo, habilida selectores dependiendo el modelo
        if (model_value.value == "Mesa_1" || model_value.value == "Mesa_2") {
            disableTxt("posSelect",false)
            disableTxt("take_putSelect",false)
            document.getElementById("text_pallet_selected").style.visibility = "hidden"
            // disableDiv("text_pallet_selected")
            current_pos_casita_value = ""
            current_take_put_value = ""
        }
        else{
            disableTxt("pos_casitaSelect",false)
            disableTxt("take_putSelect",false)
            disableTxt("pos_palletSelect",false)
            document.getElementById("text_pallet_selected").style.visibility = "visible"
            current_pos_casita_value = ""
            current_take_put_value = ""
        }
    });

    //reemplaza valores texto para seleccionar el modelo que habilita funciones
    model_value.addEventListener('change', function() {
        model_value_string = (model_value.value).toString()
        text_model_selected.innerHTML = model_value_string

        //inabilita selectores cuando se cambia de modelo
        if (model_value.value == "Mesa_1" || model_value.value == "Mesa_2") {
            disableTxt("pos_casitaSelect",true)
            disableTxt("pos_palletSelect",true)
        }
        else{
            disableTxt("posSelect",true)
        }

        //reestablece los valores del mensaje de sub rutina
        text_gripper.innerHTML = "______"
        text_pos.innerHTML = "______"
        text_take_put.innerHTML = "______"
        text_pallet.innerHTML = "______"

        //reestablece valores de los select
        pos_value.value = "Posición"
        take_put_value.value = "Tomar/Dejar"
        pos_casita_value.value = "Posición Casita"
        pos_pallet_value.value = "Pallet"

        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)

    });

    pos_value.addEventListener('change', function() {
        position_value_string = (pos_value.value).toString()
        text_pos.innerHTML = position_value_string
        text_gripper.innerHTML = "Gripper 1" // pone como valor gripper 1 al seleccionar posicion de mesa xq siempre toma o deja con gripper 1

        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)

    });

    take_put_value.addEventListener('change', function() {
        take_put_value_string = (take_put_value.value).toString()
        text_take_put.innerHTML = take_put_value_string
        //actualiza el estado actual en una variable local
        current_take_put_value = take_put_value_string

        //modifica el texto de gripper dependiendo de que se va a hacer
        if ((current_take_put_value == "Tomar") && (current_pos_casita_value == "OP 30")) {
            text_gripper.innerHTML = "Gripper 2"
        } 
        else if (current_take_put_value == "Dejar" && current_pos_casita_value == "OP 30") {
            text_gripper.innerHTML = "Gripper 1"
        }
        else if (current_take_put_value == "Tomar" && current_pos_casita_value == "OP 40"){
            text_gripper.innerHTML = "Gripper 1"
        }
        else if (current_take_put_value == "Dejar" && current_pos_casita_value == "OP 40"){
            text_gripper.innerHTML = "Gripper 2"
        }


        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)
    });

    pos_casita_value.addEventListener('change', function() {
        // console.log(pos_casita_value.value);
        position_value_string = (pos_casita_value.value).toString()
        text_pos.innerHTML = position_value_string
        //actualiza el estado actual en una variable local
        current_pos_casita_value = position_value_string
        //modifica el texto de gripper dependiendo de que se va a hacer        
        if (current_take_put_value == "Tomar" && current_pos_casita_value == "OP 30") {
            text_gripper.innerHTML = "Gripper 2"
        } 
        else if (current_take_put_value == "Dejar" && current_pos_casita_value == "OP 30") {
            text_gripper.innerHTML = "Gripper 1"
        }
        else if (current_take_put_value == "Tomar" && current_pos_casita_value == "OP 40"){
            text_gripper.innerHTML = "Gripper 1"
        }
        else if (current_take_put_value == "Dejar" && current_pos_casita_value == "OP 40"){
            text_gripper.innerHTML = "Gripper 2"
        }

        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)
    });

    pos_pallet_value.addEventListener('change', function() {
        pallet_value_string = (pos_pallet_value.value).toString()
        text_pallet.innerHTML = pallet_value_string

        //manda comando al back con lo seleccionado y el menupara rutina de semiautomatico
        const name_bit = this.options[this.selectedIndex].getAttribute("name_bit");
        console.log(name_bit);
        sendCommandSemi("semi", name_bit)

    });
    
    
    function sendCommandSemi(menu, name_bit){
        let url = "http://localhost:8000/control/semiautomatico/routine/";
        let params = "&menu=" + menu + "&name=" + name_bit;
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }

    
});