window.addEventListener("DOMContentLoaded", () => {
    (window.location.hash);
    //sensores states//
    //  const arrSensores = ['signal_0','signal_1','signal_2','signal_3','signal_4','signal_5',
    // 'signal_6','signal_7','signal_8','signal_9','signal_10','signal_11','signal_12','signal_13',
    // 'signal_14','signal_15','signal_16','signal_17','signal_18','signal_19','signal_20','signal_21',
    // 'signal_22','signal_23','signal_24','signal_25','signal_26','signal_27','signal_28','signal_29',
    // 'signal_30','signal_31','signal_32','signal_33','signal_34','signal_35','signal_36','signal_37',
    // 'signal_38','signal_39','signal_40','signal_41','signal_42','signal_43','signal_44','signal_45',
    // 'signal_46','signal_47','signal_48','signal_49','signal_50','signal_51','signal_52','signal_53',
    // 'signal_54','signal_55','signal_56','signal_57','signal_58','signal_59','signal_60','signal_61',
    // 'signal_62','signal_63','signal_64','signal_65','signal_66','signal_67','signal_68','signal_69',
    // 'signal_70','signal_71','signal_72','signal_73','signal_74','signal_75','signal_76','signal_77',
    // 'signal_78','signal_79','signal_80','signal_81','signal_82','signal_83','signal_84','signal_85',
    // 'signal_86','signal_87','signal_88','signal_89','signal_90','signal_91','signal_92','signal_93',
    // 'signal_94','signal_95','signal_96','signal_97','signal_98','signal_99','signal_101','signal_102',
    // 'signal_103','signal_104','signal_105','signal_106','signal_107','signal_108','signal_109','signal_110',
    // 'signal_111','signal_112','signal_113','signal_114','signal_115','signal_116','signal_117','signal_118',
    // 'signal_119','signal_120','signal_121','signal_122','signal_123','signal_124','signal_125','signal_126',
    // 'signal_127','signal_128','signal_129','signal_130','signal_131','signal_132','signal_133',]
    //]

    if (window.location.pathname == /mesa_1_neumatic/) {
        tablaDrawer2 = document.getElementById("tablaDrawer2")
        tablaDrawer2.style.display = 'none'
    }
    else if(window.location.pathname == /mesa_2_neumatic/) {
        tablaDrawer1 = document.getElementById("tablaDrawer1")
        tablaDrawer1.style.display = 'none'

    }

    console.log(window.location.pathname);
    function see_state_sensor(sensor_name,state,invest) {
        // console.log(sensor_name);
        const sensor_name_id = document.getElementById( sensor_name );
        // console.log(sensor_name_id);
        if (sensor_name_id){
            if (state == true){
                sensor_name_id.className = "led led-green";
                    // if(invest == true){
                    //     sensor_name_id.className = "led led-grey";
                    // }
                    // else{
                    //     sensor_name_id.className = "led led-green";
                    // }
            }
            else{
                sensor_name_id.className = "led led-grey";
            }
        }
        else{
            console.log("No existe un led con ese nombre");
        }


    }
    //sensores states//
    socket.onmessage = function (event) {
        const datosWs = JSON.parse(event.data);
        dict = datosWs.plc_sensors
        arr_of_dict = Object.keys(dict)
        for (sensor_key of arr_of_dict) {
            // console.log(sensor_key);
            if (datosWs.plc_sensors[sensor_key] == true){
                see_state_sensor(sensor_key,true)
            }
            else{
                see_state_sensor(sensor_key,false)
            }
        }
    };  
});