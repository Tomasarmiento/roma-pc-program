window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    const model_value = document.getElementById('modelSelect')
    const pos_drawer_value = document.getElementById('posSelect')
    const get_put_value = document.getElementById('take_putSelect')
    const op30_op40_value = document.getElementById('pos_casitaSelect')
    const casita1_casita2_value = document.getElementById('pos_palletSelect')


    

    const btn_semiauto = document.getElementById('btn_semiauto_routine')

    
    // disableTxt("gripperSelect",true)
    disableTxt("posSelect",true)
    disableTxt("take_putSelect",true)
    disableTxt("pos_casitaSelect",true)
    disableTxt("sub_routine_container",true)
    disableTxt("pos_palletSelect",true)



    btn_semiauto.addEventListener('click', (e) => {
        console.log('click routine');
    });


    let select = document.getElementsByTagName('select');
    let options = document.getElementsByTagName('option');
    // console.log(select);
    
    // for(let i=0; i < select.length; i++){
    //     if(select[i].hasAttribute('menu')){
    //         console.log('tiene atributo');
    //         select[i].addEventListener('change', (e) => {
    //             if(options[i].hasAttribute('menu')){
    //                 let menu = options[i].getAttribute('menu');
    //                 let name = options[i].getAttribute('id');
    //                 sendCommand(menu, name);
    //             }
    //         });
    //     }
    // }

    // for(let i=0; i < select.length; i++){
    //     if(select[i].hasAttribute('menu')){
    //         select[i].addEventListener('change', (e) => {
    //             console.log(select[i]);
    //             let menu = select[i].getAttribute('menu');
    //             for(let w=0; w < options.length; w++){
    //                 // console.log(options[w]);
    //                 if(options[w].hasAttribute('other')){
    //                     let name = options[w].getAttribute('id');
    //                     sendCommand(menu, name);
    //                 }
    //             }
    //         });
    //     }
    // }


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