from apps.ws.utils.functions import send_front_message
from apps.ws.utils.variables import frontState
from apps.parameters.utils import variables as param_vars
import http.client
from apps.control.utils import variables as control_vars
import threading
import random, time
import json
from apps.service.api.service import start_service

def values_sensors(sensor_value,sensor):#,name
    # print(sensor_value)
    dicts = param_vars.PLC_DEFAULT_VARIABLES.values()   
    for key, value in param_vars.PLC_DEFAULT_VARIABLES.items():
        # print(f"la key es:{key}, y la value es {value}")   
        if key not in dicts:
            # print("entro al if")
            param_vars.PLC_VARIABLES[key] = sensor_value
            # print(param_vars.PLC_VARIABLES[key])
        else:
            # print("entro al else")
            param_vars.PLC_VARIABLES[key] = sensor_value
    print(param_vars.PLC_VARIABLES)

def sensores_plc():
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    # lista con valores de los sensores
    DERIVED_SENSOR_STATES = []

    conn = http.client.HTTPSConnection("192.168.3.150")
    payload = json.dumps({
        "id": 0,
        "jsonrpc": "2.0",
        "method": "PlcProgram.Read", #Write #Read
        "params": {
            "var": "\"mar\".markarray[0]",#array database
            # "var": "\"OUT_13\"", #entrada salida modificar
            # "value": False  #entrada salida modificar
        }
    })

    headers = {
        'X-Auth-Token': control_vars.PLC_TOKEN['token'],
        'Content-Type': 'application/json',
    }

    for n in range(0,len(control_vars.DEFAULT_SENSOR_STATES)):
        #cambia valor del json para obtener todos los valores de los sensores
        strValue = payload
        strToReplace   = '0'
        replacementStr = str(n)
        strValue = replacementStr.join(strValue.rsplit(strToReplace, 1))

        #se manda el mensaje
        conn.request("POST", "/api/jsonrpc", strValue, headers)
        res = conn.getresponse()
        data = res.read()
        data_json = data.decode("utf-8")
        data_parsed = json.loads(data_json)
        sensor_value = data_parsed["result"]
        # print(f"El valor que trae del plc es{sensor_value}")
        #append de los valores a la lista
        DERIVED_SENSOR_STATES.append(sensor_value)

    return DERIVED_SENSOR_STATES

def derived_sensores_states(list_state_sensores):
    print("lista de sensores del plc",list_state_sensores)
    dicts = control_vars.PLC_DEFAULT_VARIABLES.values() 
    for n in range(0,len(list_state_sensores)):
        for w in range(0,len(control_vars.PLC_DEFAULT_VARIABLES)):
            # print(control_vars.PLC_DEFAULT_VARIABLES[f'signal_{n}'])
            if n == w:
                control_vars.PLC_DEFAULT_VARIABLES[f'signal_{n}'] = list_state_sensores[n]
                # list(dicts)[w] = list_state_sensores[n]
        # dicts = list_state_sensores[n]
    print("lista de sensores local",control_vars.PLC_DEFAULT_VARIABLES,)
    return control_vars.PLC_DEFAULT_VARIABLES


# def get_front_states():
#     data = {'hola':10}
#     return data

# data = get_front_states()
# send_front_message(data)
# print("hola")





# class FrontWs(threading.Thread):

#     def __init__(self, **kwargs):
#         super(FrontWs, self).__init__(**kwargs)
    
#     def run(self):
#         time.sleep(3)
#         while 1:
#             data = {
#                 'mesa_armado_1' : int(param_vars.PARAMS['mesa_armado_1']),
#                 'mesa_armado_2' : int(param_vars.PARAMS['mesa_armado_2']),
#                 'okuma_1' : int(param_vars.PARAMS['okuma_1']),
#                 'okuma_2' : int(param_vars.PARAMS['okuma_2']),
#                 'okuma_3' : int(param_vars.PARAMS['okuma_3']),
#                 'okuma_4' : int(param_vars.PARAMS['okuma_4']),
#                 'led_state': frontState.led_on,
#             }
#             send_front_message(data)
#             time.sleep(3)


# class FrontWs():
#     start_service()
#     # send_front_message(data)
#     time.sleep(3)
