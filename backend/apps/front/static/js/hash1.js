window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    let btn_on_led = document.getElementById('prender');
    let btn_off_led = document.getElementById('apagar');
       
    btn_on_led.addEventListener('click', (e) => {
    let url = "http://localhost:8000/control/test-led/on/";

    let xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);

    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhr.send();
  });
  
  btn_off_led.addEventListener('click', (e) => {
    let url = "http://localhost:8000/control/test-led/off/";

    let xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);

    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhr.send();
  });

});