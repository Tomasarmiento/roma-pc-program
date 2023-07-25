window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    const hash_automatic = document.getElementById("auto_hash")
    const hash_semi = document.getElementById("semi_hash")
    const hash_manual = document.getElementById("manual_hash")
    const index_leyend = document.getElementById("index_leyend")


    hash_automatic.addEventListener('click', (e) => {
        sendCommandChangeModeRoutine("auto_routine_change")
        
    });

    hash_semi.addEventListener('click', (e) => {
        sendCommandChangeModeRoutine("semi_routine_change")
    });

    hash_manual.addEventListener('click', (e) => {
        if (confirm(`Al pasar al modo manual el modo automatico volvera al paso 0, DESEA CONTINUAR?`)) {
            sendCommandChangeModeRoutine("manual_routine_change")
            window.location.href="http://localhost:8000/neumatic_index/";
        }
        else {
            console.log("Cancelled");
        }
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

    console.log(window.location.pathname);

    if (window.location.pathname != "/index/"){
        index_leyend.style.display = "none";
    }

   
});