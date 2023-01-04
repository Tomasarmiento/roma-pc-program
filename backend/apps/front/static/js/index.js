window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    const hash_automatic = document.getElementById("auto_hash")
    const hash_semi = document.getElementById("semi_hash")
    const hash_manual = document.getElementById("manual_hash")
    const hash_login = document.getElementById("login_hash")
    const hash_logout = document.getElementById("logout_hash")
    const hash_desactivar_okuma = document.getElementById("desactivar_okuma_hash")
    const hash_errores_hash = document.getElementById("errores_hash")
    const hash_index = document.getElementById("index_hash")
    const index_leyend = document.getElementById("index_leyend")
    


    hash_automatic.addEventListener('click', (e) => {
        sendCommandChangeModeRoutine("auto_routine_change")
    });
    hash_semi.addEventListener('click', (e) => {
        sendCommandChangeModeRoutine("semi_routine_change")
    });
    hash_manual.addEventListener('click', (e) => {
        sendCommandChangeModeRoutine("manual_routine_change")
    });
    hash_login.addEventListener('click', (e) => {
        sendCommandChangeModeRoutine("login_routine_change")
    });
    hash_index.addEventListener('click', (e) => {
        sendCommandChangeModeRoutine("index_hash")
    });
    if (hash_logout) {
        hash_logout.addEventListener('click', (e) => {
            sendCommandChangeModeRoutine("logout_routine_change")
        });
    }
    if (hash_desactivar_okuma) {
        hash_desactivar_okuma.addEventListener('click', (e) => {
            sendCommandChangeModeRoutine("desactivar_okuma_routine_change")
        });
    }
    hash_errores_hash.addEventListener('click', (e) => {
        sendCommandChangeModeRoutine("errores_routine_change")
    });



    function sendCommandChangeModeRoutine(hash_routine_change){
        let url = "http://localhost:8000/control/index_change/";
        let params = "&hash_routine_change=" + hash_routine_change;
        console.log('send command hash routine');
    
        // var params = "lorem=ipsum&name=alpha";
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
    
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
        xhr.send(params);
    }


    if (window.location.pathname != "/index/"){
        index_leyend.style.display = "none";
    }

    // window.addEventListener("beforeunload", function (event) {
    //     console.log(window.location.pathname);

    //     //your code goes here on location change 
    //  });



   
    
});


