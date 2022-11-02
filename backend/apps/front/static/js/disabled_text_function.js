function disableTxt(id,gripper_disabled) {
    if (gripper_disabled == true){
        document.getElementById(id).disabled = true;
    }
    else{
        document.getElementById(id).disabled = false;
    }
}


function disableDivExeptValue(element_to_show,list_of_tables) {
    for (n of list_of_tables) {
        value_unable = document.getElementById(n)
        // console.log(sensor_key);
        if (n != element_to_show){
            const value_unable = document.getElementById(n)
            value_unable.style.display = 'none'
        }
        else{
            value_unable.style.display = ""
        }
    }
}

function disableDiv(element_to_hide) {
    const value_unable = document.getElementById(element_to_hide)
    value_unable.style.display = 'none'
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