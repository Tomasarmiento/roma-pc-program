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


   btn_move_table1.addEventListener("click", () =>{
        if(model_value.value != "Mesa de armado");{
            //selector de modelo, habilida selectores dependiendo el modelo
            if (model_value.value == "Mesa_1" || model_value.value == "Mesa_2") {
                disableTxt("gripperSelect",false)
                disableTxt("posSelect",false)
                disableTxt("take_putSelect",false)
                document.getElementById('sub_routine_container').style = "visibility: visible;"
            }
            else{
                disableTxt("gripperSelect",false)
                disableTxt("pos_casitaSelect",false)
                disableTxt("take_putSelect",false)
                document.getElementById('sub_routine_container').style = "visibility: visible;"
            }
        }
    });

    //reemplaza valores texto para seleccionar el modelo que habilita funciones
    model_value.addEventListener('change', function() {
        model_value_string = (model_value.value).toString()
        text_model_selected.innerHTML = model_value_string

        //inabilita selectores cuando se cambia de modelo
        disableTxt("gripperSelect",true)
        disableTxt("posSelect",true)
        disableTxt("take_putSelect",true)
        disableTxt("pos_casitaSelect",true)
        document.getElementById('sub_routine_container').style = "visibility: hidden;"

        //reestablece los valores del mensaje de sub rutina
        text_gripper.innerHTML = "______"
        text_pos.innerHTML = "______"
        text_take_put.innerHTML = "______"

        //reestablece valores de los select
        gripper_value.value = "Gripper"
        pos_value.value = "Posición"
        take_put_value.value = "Tomar/Dejar"
        pos_casita_value.value = "Posición Casita"

    });

    //reemplaza valores en texto para ejecutar rutina
    gripper_value.addEventListener('change', function() {
        gripper_value_string = (gripper_value.value).toString()
        text_gripper.innerHTML = gripper_value_string
    });

    pos_value.addEventListener('change', function() {
        position_value_string = (pos_value.value).toString()
        text_pos.innerHTML = position_value_string
    });

    take_put_value.addEventListener('change', function() {
        take_put_value_string = (take_put_value.value).toString()
        text_take_put.innerHTML = take_put_value_string
    });

    pos_casita_value.addEventListener('change', function() {
        position_value_string = (pos_casita_value.value).toString()
        text_pos.innerHTML = position_value_string
    });
});