window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    // console.log(window.location);
    const okuma_value = document.getElementById('okumaSelect')
    const mesa_value = document.getElementById('mesaSelect')
    const gripper_value = document.getElementById('gripperSelect')
    const changeMachineBtn = document.getElementById('changeMachineBtn')


    if (window.location.pathname != "/semiAutomatico/"){
        okuma_value.addEventListener('change', function() {
            // console.log('You selected: ', okuma_value.value);
            // let hola = okuma_value.value
            okuma_selected_model(okuma_value.value)
            //reedireccionamiento
            redirectModelMachine(okuma_value.value)
            // console.log(okuma_value.value);
            // let model_machine = hola.getAttribute('model_machine');
            // console.log(model_machine);
        });
        mesa_value.addEventListener('change', function() {
            //reedireccionamiento
            redirectModelTable(mesa_value.value)
            table_selected_model(mesa_value.value)
        });
        gripper_value.addEventListener('change', function() {
            //reedireccionamiento
            redirectGripper(gripper_value.value)
            startRoutine(gripper_value.value)
        });
    }


    function okuma_selected_model(model_machine){
        let url = "http://localhost:8000/control/sensores/okuma/";
        let params = "model_machine=" + model_machine;
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }

    function table_selected_model(model_table){
        let url = "http://localhost:8000/control/sensores/mesa/";
        let params = "model_table=" + model_table;
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }

    function redirectModelMachine(hash) {
        switch(hash){
            case 'Okuma_1':
                console.log('es el okuma 1');
                window.location.href="http://localhost:8000/okuma_1_neumatic/";
                break
            case 'Okuma_2':
                console.log('es el okuma 2');
                window.location.href="http://localhost:8000/okuma_2_neumatic/";
                break
            case 'Okuma_3':
                console.log('es el okuma 3');
                window.location.href="http://localhost:8000/okuma_3_neumatic/";
                break
            case 'Okuma_4':
                console.log('es el okuma 4');
                window.location.href="http://localhost:8000/okuma_4_neumatic/";
                break
        }
    }

    function redirectModelTable(hash) {
        switch(hash){
            case 'Mesa_1':
                console.log('es la mesa 1');
                window.location.href="http://localhost:8000/mesa_1_neumatic/";
                break
            case 'Mesa_2':
                console.log('es la mesa 2');
                window.location.href="http://localhost:8000/mesa_2_neumatic/";
                break
        }
    }

    function redirectGripper(hash) {
        switch(hash){
            case 'Gripper_1/Gripper_2':
                console.log('es el gripper 1,2');
                window.location.href="http://localhost:8000/gripper_neumatic/";
                break
        }
    }

    //Get the button
    var mybutton = document.getElementById("boton_neumatic");

    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            mybutton.style.display = "block";
        } else {
            mybutton.style.display = "none";
        }
    }
    
    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
    }
    mybutton.addEventListener("click", () =>{
        topFunction()
    });

    
    // changeMachineBtn.addEventListener('click', (e) => {
    //     let model_machine = btn_cabezal.getAttribute('model_machine');
    //     startRoutine(model_machine);
    //     // redirectModelMachine(model_machine);
       
    // });


   
});