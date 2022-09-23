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
   //VALOR DE LOS SELECT
   const model_value = document.getElementById('modelSelect')
   const gripper_value = document.getElementById('gripperSelect')
   const pos_value = document.querySelector('#posSelect')
   const take_put_value = document.querySelector('#take_putSelect')
   const pos_casita_value = document.querySelector('#pos_casitaSelect')
   //VARIABLES PARA ACTUALIZAR LOS MODELOS SELECCIONADOS LOCALES
   var current_pos_casita_value = ""
   var current_take_put_value = ""


//    btn_move_table1.addEventListener("click", () =>{
//         console.log(model_value.value)
//         if(model_value.value != "Mesas de armado");{ 
//             //selector de modelo, habilida selectores dependiendo el modelo
//             if (model_value.value == "Mesa_1" || model_value.value == "Mesa_2") {
//                 // disableTxt("gripperSelect",false)
//                 disableTxt("posSelect",false)
//                 disableTxt("take_putSelect",false)
//                 document.getElementById('sub_routine_container').style = "visibility: visible;"
//             }
//             else{
//                 // disableTxt("gripperSelect",false)
//                 disableTxt("pos_casitaSelect",false)
//                 disableTxt("take_putSelect",false)
//                 document.getElementById('sub_routine_container').style = "visibility: visible;"
//             }
//         }
//     });

    model_value.addEventListener("change", () =>{
        //selector de modelo, habilida selectores dependiendo el modelo
        if (model_value.value == "Mesa_1" || model_value.value == "Mesa_2") {
            // disableTxt("gripperSelect",false)
            disableTxt("posSelect",false)
            disableTxt("take_putSelect",false)
            current_pos_casita_value = ""
            current_take_put_value = ""
            // document.getElementById('sub_routine_container').style = "visibility: visible;"
        }
        else{
            // disableTxt("gripperSelect",false)
            disableTxt("pos_casitaSelect",false)
            disableTxt("take_putSelect",false)
            current_pos_casita_value = ""
            current_take_put_value = ""
            // document.getElementById('sub_routine_container').style = "visibility: visible;"
        }
});

    //reemplaza valores texto para seleccionar el modelo que habilita funciones
    model_value.addEventListener('change', function() {
        model_value_string = (model_value.value).toString()
        text_model_selected.innerHTML = model_value_string

        //inabilita selectores cuando se cambia de modelo
        if (model_value.value == "Mesa_1" || model_value.value == "Mesa_2") {
            disableTxt("pos_casitaSelect",true)
        }
        else{
            disableTxt("posSelect",true)
        }
        
        //disableTxt("gripperSelect",true)
        // disableTxt("posSelect",true)
        // disableTxt("take_putSelect",true)
        // disableTxt("pos_casitaSelect",true)
        // document.getElementById('sub_routine_container').style = "visibility: hidden;"

        //reestablece los valores del mensaje de sub rutina
        text_gripper.innerHTML = "______"
        text_pos.innerHTML = "______"
        text_take_put.innerHTML = "______"

        //reestablece valores de los select
        // gripper_value.value = "Gripper"
        pos_value.value = "Posición"
        take_put_value.value = "Tomar/Dejar"
        pos_casita_value.value = "Posición Casita"

    });

    //reemplaza valores en texto para ejecutar rutina
    // gripper_value.addEventListener('change', function() {
    //     gripper_value_string = (gripper_value.value).toString()
    //     text_gripper.innerHTML = gripper_value_string
    // });

    pos_value.addEventListener('change', function() {
        position_value_string = (pos_value.value).toString()
        text_pos.innerHTML = position_value_string
        text_gripper.innerHTML = "Gripper 1" // pone como valor gripper 1 al seleccionar posicion de mesa xq siempre toma o deja con gripper 1

    });

    take_put_value.addEventListener('change', function() {
        take_put_value_string = (take_put_value.value).toString()
        console.log(take_put_value_string);
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

    });

    

    
});