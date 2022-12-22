window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    let btn_on_led = document.getElementById('prender');
    let btn_off_led = document.getElementById('apagar');
    let btn_test_plc = document.getElementById('plc_test');
    let btn_test_msg = document.getElementById('msg_test');
    let btn_mensaje_testeo = document.getElementById('mensaje_test');
    let btn_javascript = document.getElementById('javascript');
       
    btn_on_led.addEventListener('click', (e) => {
    let url = "http://localhost:8000/control/test-led/on/"; //"http://192.168.3.127:8000/control/test-led/on/"

    let xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);

    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhr.send();
  });

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

  btn_javascript.addEventListener('click', (e) => {
    // WARNING: For POST requests, body is set to null by browsers.
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

    xhr.addEventListener("readystatechange", function() {
      if(this.readyState === 4) {
        console.log(this.responseText);
      }
    });

    xhr.open("POST", "https://192.168.3.150/api/jsonrpc");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send(data);
  });




  function envioComando() {
    var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://192.168.3.150/api/jsonrpc',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "id": 0,
    "jsonrpc": "2.0",
    "method": "Api.Login",
    "params": {
      "user": "user",
      "password": "1234"
    }
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
  }

});