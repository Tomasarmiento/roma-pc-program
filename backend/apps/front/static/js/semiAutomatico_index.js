window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    const okuma_value = document.getElementById('okumaSelect')
    const mesa_value = document.getElementById('mesaSelect')
    const gripper_value = document.getElementById('gripperSelect')
    const changeMachineBtn = document.getElementById('changeMachineBtn')
    const mover_robot_text = document.querySelector('#mover_robot')
    const pos_value = document.querySelector('#posSelect')

    
    // disableTxt("gripperSelect",true)
    disableTxt("posSelect",true)
    disableTxt("take_putSelect",true)
    disableTxt("pos_casitaSelect",true)
    disableTxt("sub_routine_container",true)

    // okuma_value.addEventListener('change', function() {
    //     //reedireccionamiento
    //     redirectModelMachine(okuma_value.value)
    // });
    // mesa_value.addEventListener('change', function() {
    //     //reedireccionamiento
    //     redirectModelTable(mesa_value.value)
    // });
    // gripper_value.addEventListener('change', function() {
    //     //reedireccionamiento
    //     // redirectGripper(gripper_value.value)
    // });

    // function redirectModelMachine(hash) {
    //     switch(hash){
    //         case 'Okuma_1':
    //             console.log('es el okuma 1');
    //             window.location.href="http://localhost:8000/okuma_1_semiAutomatico/";
    //             break
    //         case 'Okuma_2':
    //             console.log('es el okuma 2');
    //             window.location.href="http://localhost:8000/okuma_2_semiAutomatico/";
    //             break
    //         case 'Okuma_3':
    //             console.log('es el okuma 3');
    //             window.location.href="http://localhost:8000/okuma_3_semiAutomatico/";
    //             break
    //         case 'Okuma_4':
    //             console.log('es el okuma 4');
    //             window.location.href="http://localhost:8000/okuma_4_semiAutomatico/";
    //             break
    //     }
    // }

    // function redirectModelTable(hash) {
    //     switch(hash){
    //         case 'Mesa_1':
    //             console.log('es la mesa 1');
    //             window.location.href="http://localhost:8000/mesa_1_semiAutomatico/";
    //             break
    //         case 'Mesa_2':
    //             console.log('es la mesa 2');
    //             window.location.href="http://localhost:8000/mesa_2_semiAutomatico/";
    //             break
    //     }
    // }
});
// export const nombre = "tomas";