window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    const btn_desactivate_okuma_1 = document.getElementById('desactivate_ok1')
    const btn_desactivate_okuma_2 = document.getElementById('desactivate_ok2')
    const btn_desactivate_okuma_3 = document.getElementById('desactivate_ok3')
    const btn_desactivate_okuma_4 = document.getElementById('desactivate_ok4')

    const btn_desactivate_mesa_1 = document.getElementById('desactivate_me1')
    const btn_desactivate_mesa_2 = document.getElementById('desactivate_me2')



    btn_desactivate_okuma_1.addEventListener('click', (e) => {
        disable_okuma('okuma_1')
    });

    btn_desactivate_okuma_2.addEventListener('click', (e) => {
        disable_okuma('okuma_2')
    });

    btn_desactivate_okuma_3.addEventListener('click', (e) => {
        disable_okuma('okuma_3')
    });

    btn_desactivate_okuma_4.addEventListener('click', (e) => {
        disable_okuma('okuma_4')
    });

    function disable_okuma(model_machine){
        let url = "http://localhost:8000/control/automatico/okuma/";
        let params = "model_machine=" + model_machine;
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }

});