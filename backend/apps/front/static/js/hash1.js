window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    let btn_on_led = document.getElementById('prender');
    let btn_off_led = document.getElementById('apagar');
    let btn_test_plc = document.getElementById('plc_test');
    let btn_test_msg = document.getElementById('msg_test');
    let btn_mensaje_testeo = document.getElementById('mensaje_test');
       
    btn_on_led.addEventListener('click', (e) => {
    let url = "http://localhost:8000/control/test-led/on/"; //"http://192.168.3.127:8000/control/test-led/on/"

    let xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);

    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhr.send();
  });
  mensaje_test

  btn_mensaje_testeo.addEventListener('click', (e) => {
    let url = "http://localhost:8000/control/msge-test/";//"http://192.168.3.127:8000/control/test-led/off/"

    let xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);

    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhr.send();
  });

  btn_test_msg.addEventListener('click', (e) => {
    let url = "http://localhost:8000/control/test-led/off/";//"http://192.168.3.127:8000/control/test-led/off/"

    let xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);

    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhr.send();
  });
  
  // btn_test_plc.addEventListener('click', (e) => {
  //   let url = "https://192.168.3.150/api/jsonrpc";

  //   let xhr = new XMLHttpRequest();

  //   xhr.open("POST", url, true);

  //   //Send the proper header information along with the request
  //   xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

  //   xhr.send();
  // });

  btn_test_plc.addEventListener('click', (e) => {
    envioComando()
  });




  function envioComando() {
    var data = JSON.stringify({
      "id": 0,
      "jsonrpc": "2.0",
      "method": "Api.Login",
      "params": {
        "user": "user",
        "password": "1234"
      }
    });
    
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    xhr.rejectUnauthorized = false;
    xhr.addEventListener("readystatechange", function() {
      if(this.readyState === 4) {
        console.log(this.responseText);
      }
    });
    
    xhr.open("POST", "https://192.168.3.150/api/jsonrpc", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    
    xhr.send(data);
  }

});