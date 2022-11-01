window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    // console.log("dentro de indexjs");
    hash_automatic = document.getElementById("auto_hash")
    hash_semi = document.getElementById("semi_hash")

    // console.log(hash_automatic);


    hash_automatic.addEventListener('click', (e) => {
        // console.log('click en hash automatic');
        sendCommandChangeModeRoutine("auto_routine_change")
    });

    hash_semi.addEventListener('click', (e) => {
        // console.log('click en hash automatic');
        sendCommandChangeModeRoutine("semi_routine_change")
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
   
});