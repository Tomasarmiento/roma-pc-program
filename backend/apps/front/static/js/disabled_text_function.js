function disableTxt(id,gripper_disabled) {
    if (gripper_disabled == true){
        document.getElementById(id).disabled = true;
    }
    else{
        document.getElementById(id).disabled = false;
    }
}
