from apps.ws.utils.functions import send_front_message
from apps.ws.utils.variables import frontState
from apps.parameters.utils import variables as param_vars
import http.client
from apps.control.utils import variables as control_vars
import threading
import random, time
import json
from apps.service.api.service import start_service

from apps.control.utils.variables import PLC_TOKEN,LIST_OF_DIRECTIONS,PLC_DEFAULT_VARIABLES

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

    for n in range(0,len(control_vars.PLC_DEFAULT_VARIABLES)):
        # print(len(control_vars.PLC_DEFAULT_VARIABLES))
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
    print(DERIVED_SENSOR_STATES)
    count_true = 0
    count_false = 0
    for n in (DERIVED_SENSOR_STATES):
        if n == True:
            count_true +=1
        else:
            count_false +=1
    print(count_false,count_true)
    return DERIVED_SENSOR_STATES

def derived_sensores_states(list_state_sensores):
    # print("lista de sensores del plc",list_state_sensores)
    dicts = control_vars.PLC_DEFAULT_VARIABLES.values() 
    for n in range(0,len(list_state_sensores)):
        for w in range(0,len(control_vars.PLC_DEFAULT_VARIABLES)):
            # print(control_vars.PLC_DEFAULT_VARIABLES[f'signal_{n}'])
            if n == w:
                control_vars.PLC_DEFAULT_VARIABLES[f'signal_{n}'] = list_state_sensores[n]
                # list(dicts)[w] = list_state_sensores[n]
        # dicts = list_state_sensores[n]
    # print("lista de sensores local",control_vars.PLC_DEFAULT_VARIABLES,)
    return control_vars.PLC_DEFAULT_VARIABLES

def switch_led_state_off():
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    conn = http.client.HTTPSConnection("192.168.3.150")
    payload = json.dumps([
    # {"jsonrpc":"2.0","id":"1","method":"PlcProgram.Read","params":{"var":"\"CH1_I_RA\""}},
    # {"jsonrpc":"2.0","id":"2","method":"PlcProgram.Read","params":{"var":"\"CH1_I_AL\""}},
    # {"jsonrpc":"2.0","id":"3","method":"PlcProgram.Read","params":{"var":"\"CH1_I_ID\""}},
    # {"jsonrpc":"2.0","id":"4","method":"PlcProgram.Read","params":{"var":"\"CH1_I_MB\""}},
    # {"jsonrpc":"2.0","id":"5","method":"PlcProgram.Read","params":{"var":"\"CH1_I_PS\""}},
    # {"jsonrpc":"2.0","id":"6","method":"PlcProgram.Read","params":{"var":"\"CH1_I_HO\""}},
    # {"jsonrpc":"2.0","id":"7","method":"PlcProgram.Read","params":{"var":"\"CH1_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"8","method":"PlcProgram.Read","params":{"var":"\"CH1_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"9","method":"PlcProgram.Read","params":{"var":"\"CH2_I_RA\""}},
    # {"jsonrpc":"2.0","id":"10","method":"PlcProgram.Read","params":{"var":"\"CH2_I_AL\""}},
    # {"jsonrpc":"2.0","id":"11","method":"PlcProgram.Read","params":{"var":"\"CH2_I_ID\""}},
    # {"jsonrpc":"2.0","id":"12","method":"PlcProgram.Read","params":{"var":"\"CH2_I_MB\""}},
    # {"jsonrpc":"2.0","id":"13","method":"PlcProgram.Read","params":{"var":"\"CH2_I_PS\""}},
    # {"jsonrpc":"2.0","id":"14","method":"PlcProgram.Read","params":{"var":"\"CH2_I_HO\""}},
    # {"jsonrpc":"2.0","id":"15","method":"PlcProgram.Read","params":{"var":"\"CH2_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"16","method":"PlcProgram.Read","params":{"var":"\"CH2_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"17","method":"PlcProgram.Read","params":{"var":"\"CH3_I_RA\""}},
    # {"jsonrpc":"2.0","id":"18","method":"PlcProgram.Read","params":{"var":"\"CH3_I_AL\""}},
    # {"jsonrpc":"2.0","id":"19","method":"PlcProgram.Read","params":{"var":"\"CH3_I_ID\""}},
    # {"jsonrpc":"2.0","id":"20","method":"PlcProgram.Read","params":{"var":"\"CH3_I_MB\""}},
    # {"jsonrpc":"2.0","id":"21","method":"PlcProgram.Read","params":{"var":"\"CH3_I_PS\""}},
    # {"jsonrpc":"2.0","id":"22","method":"PlcProgram.Read","params":{"var":"\"CH3_I_HO\""}},
    # {"jsonrpc":"2.0","id":"23","method":"PlcProgram.Read","params":{"var":"\"CH3_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"24","method":"PlcProgram.Read","params":{"var":"\"CH3_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"25","method":"PlcProgram.Read","params":{"var":"\"CH4_I_RA\""}},
    # {"jsonrpc":"2.0","id":"26","method":"PlcProgram.Read","params":{"var":"\"CH4_I_AL\""}},
    # {"jsonrpc":"2.0","id":"27","method":"PlcProgram.Read","params":{"var":"\"CH4_I_ID\""}},
    # {"jsonrpc":"2.0","id":"28","method":"PlcProgram.Read","params":{"var":"\"CH4_I_MB\""}},
    # {"jsonrpc":"2.0","id":"29","method":"PlcProgram.Read","params":{"var":"\"CH4_I_PS\""}},
    # {"jsonrpc":"2.0","id":"30","method":"PlcProgram.Read","params":{"var":"\"CH4_I_HO\""}},
    # {"jsonrpc":"2.0","id":"31","method":"PlcProgram.Read","params":{"var":"\"CH4_I_NPA\""}},
    # {"jsonrpc":"2.0","id":"32","method":"PlcProgram.Read","params":{"var":"\"CH4_I_NPR\""}},
    # {"jsonrpc":"2.0","id":"33","method":"PlcProgram.Read","params":{"var":"\"R_I_AL\""}},
    # {"jsonrpc":"2.0","id":"34","method":"PlcProgram.Read","params":{"var":"\"R_I_HF\""}},
    # {"jsonrpc":"2.0","id":"35","method":"PlcProgram.Read","params":{"var":"\"R_I_ID\""}},
    # {"jsonrpc":"2.0","id":"36","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_0\""}},
    # {"jsonrpc":"2.0","id":"37","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_1\""}},
    # {"jsonrpc":"2.0","id":"38","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_2\""}},
    # {"jsonrpc":"2.0","id":"39","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_3\""}},
    # {"jsonrpc":"2.0","id":"40","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_4\""}},
    # {"jsonrpc":"2.0","id":"41","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_5\""}},
    # {"jsonrpc":"2.0","id":"42","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_6\""}},
    # {"jsonrpc":"2.0","id":"43","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_7\""}},
    # {"jsonrpc":"2.0","id":"44","method":"PlcProgram.Read","params":{"var":"\"R_I_G1_PS\""}},
    # {"jsonrpc":"2.0","id":"45","method":"PlcProgram.Read","params":{"var":"\"R_I_G2_PS\""}},
    # {"jsonrpc":"2.0","id":"46","method":"PlcProgram.Read","params":{"var":"\"R_I_FLS\""}},
    # {"jsonrpc":"2.0","id":"47","method":"PlcProgram.Read","params":{"var":"\"R_I_RLS\""}},
    # {"jsonrpc":"2.0","id":"48","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_PS_1\""}},
    # {"jsonrpc":"2.0","id":"49","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_PS_2\""}},
    # {"jsonrpc":"2.0","id":"50","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_PS_1\""}},
    # {"jsonrpc":"2.0","id":"51","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_PS_2\""}},
    # {"jsonrpc":"2.0","id":"52","method":"PlcProgram.Read","params":{"var":"\"MA1_I_GS_UP\""}},
    # {"jsonrpc":"2.0","id":"53","method":"PlcProgram.Read","params":{"var":"\"MA1_I_GS_DN\""}},
    # {"jsonrpc":"2.0","id":"54","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_ES_1\""}},
    # {"jsonrpc":"2.0","id":"55","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_ES_2\""}},
    # {"jsonrpc":"2.0","id":"56","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_ES_1\""}},
    # {"jsonrpc":"2.0","id":"57","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_ES_2\""}},
    # {"jsonrpc":"2.0","id":"58","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_NS\""}},
    # {"jsonrpc":"2.0","id":"59","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_NS\""}},
    # {"jsonrpc":"2.0","id":"60","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_1_SA\""}},
    # {"jsonrpc":"2.0","id":"61","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_1_SR\""}},
    # {"jsonrpc":"2.0","id":"62","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_2_SA\""}},
    # {"jsonrpc":"2.0","id":"63","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_2_SR\""}},
    # {"jsonrpc":"2.0","id":"64","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_1_SA\""}},
    # {"jsonrpc":"2.0","id":"65","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_1_SR\""}},
    # {"jsonrpc":"2.0","id":"66","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_2_SA\""}},
    # {"jsonrpc":"2.0","id":"67","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_2_SR\""}},
    # {"jsonrpc":"2.0","id":"68","method":"PlcProgram.Read","params":{"var":"\"MA1_I_OB\""}},
    # {"jsonrpc":"2.0","id":"69","method":"PlcProgram.Read","params":{"var":"\"MA1_I_EMS\""}},
    # {"jsonrpc":"2.0","id":"70","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_PS_1\""}},
    # {"jsonrpc":"2.0","id":"71","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_PS_2\""}},
    # {"jsonrpc":"2.0","id":"72","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_PS_1\""}},
    # {"jsonrpc":"2.0","id":"73","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_PS_2\""}},
    # {"jsonrpc":"2.0","id":"74","method":"PlcProgram.Read","params":{"var":"\"MA2_I_GS_UP\""}},
    # {"jsonrpc":"2.0","id":"75","method":"PlcProgram.Read","params":{"var":"\"MA2_I_GS_DN\""}},
    # {"jsonrpc":"2.0","id":"76","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_ES_1\""}},
    # {"jsonrpc":"2.0","id":"77","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_ES_2\""}},
    # {"jsonrpc":"2.0","id":"78","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_ES_1\""}},
    # {"jsonrpc":"2.0","id":"79","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_ES_2\""}},
    # {"jsonrpc":"2.0","id":"80","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_NS\""}},
    # {"jsonrpc":"2.0","id":"81","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_NS\""}},
    # {"jsonrpc":"2.0","id":"82","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_1_SA\""}},
    # {"jsonrpc":"2.0","id":"83","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_1_SR\""}},
    # {"jsonrpc":"2.0","id":"84","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_2_SA\""}},
    # {"jsonrpc":"2.0","id":"85","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_2_SR\""}},
    # {"jsonrpc":"2.0","id":"86","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_1_SA\""}},
    # {"jsonrpc":"2.0","id":"87","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_1_SR\""}},
    # {"jsonrpc":"2.0","id":"88","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_2_SA\""}},
    # {"jsonrpc":"2.0","id":"89","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_2_SR\""}},
    # {"jsonrpc":"2.0","id":"90","method":"PlcProgram.Read","params":{"var":"\"MA2_I_OB\""}},
    # {"jsonrpc":"2.0","id":"91","method":"PlcProgram.Read","params":{"var":"\"MA2_I_EMS\""}},
    # {"jsonrpc":"2.0","id":"92","method":"PlcProgram.Read","params":{"var":"\"GRL_I_EMS\""}},
    # {"jsonrpc":"2.0","id":"93","method":"PlcProgram.Read","params":{"var":"\"System_Active\""}},
    # {"jsonrpc":"2.0","id":"94","method":"PlcProgram.Read","params":{"var":"\"Start_system_button\""}},
    # {"jsonrpc":"2.0","id":"95","method":"PlcProgram.Read","params":{"var":"\"Stop_system_button\""}},
    # {"jsonrpc":"2.0","id":"96","method":"PlcProgram.Read","params":{"var":"\"Emergency\""}},
    # {"jsonrpc":"2.0","id":"97","method":"PlcProgram.Read","params":{"var":"\"Robot_GO\""}},
    # {"jsonrpc":"2.0","id":"98","method":"PlcProgram.Read","params":{"var":"\"Robot_IDLE\""}},
    # {"jsonrpc":"2.0","id":"99","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRU1\""}},
    # {"jsonrpc":"2.0","id":"100","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_1_OP40\""}},
    # {"jsonrpc":"2.0","id":"101","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRU2\""}},
    # {"jsonrpc":"2.0","id":"102","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_2_OP40\""}},
    # {"jsonrpc":"2.0","id":"103","method":"PlcProgram.Read","params":{"var":"\"Gen_Program\""}},
    # {"jsonrpc":"2.0","id":"104","method":"PlcProgram.Read","params":{"var":"\"unblock_pallet\""}},
    # {"jsonrpc":"2.0","id":"105","method":"PlcProgram.Read","params":{"var":"\"unblocked_pallet_sensor\""}},
    # {"jsonrpc":"2.0","id":"106","method":"PlcProgram.Read","params":{"var":"\"neumatic_forward\""}},
    # {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Read","params":{"var":"\"neumatic_advance\""}},
    # {"jsonrpc":"2.0","id":"108","method":"PlcProgram.Read","params":{"var":"\"INF30\""}},
    # {"jsonrpc":"2.0","id":"109","method":"PlcProgram.Read","params":{"var":"\"Blower\""}},
    # {"jsonrpc":"2.0","id":"110","method":"PlcProgram.Read","params":{"var":"\"Booster\""}},
    # {"jsonrpc":"2.0","id":"111","method":"PlcProgram.Read","params":{"var":"\"INF40\""}},
    # {"jsonrpc":"2.0","id":"112","method":"PlcProgram.Read","params":{"var":"\"pallet_sensor\""}},
    # {"jsonrpc":"2.0","id":"113","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_1_OP20\""}},
    # {"jsonrpc":"2.0","id":"114","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_2_OP20\""}},
    # {"jsonrpc":"2.0","id":"115","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_1_OP20\""}},
    # {"jsonrpc":"2.0","id":"116","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_2_OP20\""}},
    # {"jsonrpc":"2.0","id":"117","method":"PlcProgram.Read","params":{"var":"\"OP20_available\""}},
    # {"jsonrpc":"2.0","id":"118","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRD1\""}},
    # {"jsonrpc":"2.0","id":"119","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_2_OP40\""}},
    # {"jsonrpc":"2.0","id":"120","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRD2\""}},
    # {"jsonrpc":"2.0","id":"121","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_1_OP40\""}},
    # {"jsonrpc":"2.0","id":"122","method":"PlcProgram.Read","params":{"var":"\"R_I_MA1F\""}},
    # {"jsonrpc":"2.0","id":"123","method":"PlcProgram.Read","params":{"var":"\"R_I_MA2F\""}},
    # {"jsonrpc":"2.0","id":"124","method":"PlcProgram.Read","params":{"var":"\"okuma_available\""}},
    # {"jsonrpc":"2.0","id":"125","method":"PlcProgram.Read","params":{"var":"\"M_PRG_0\""}},
    # {"jsonrpc":"2.0","id":"126","method":"PlcProgram.Read","params":{"var":"\"M_PRG_1\""}},
    # {"jsonrpc":"2.0","id":"127","method":"PlcProgram.Read","params":{"var":"\"M_PRG_2\""}},
    # {"jsonrpc":"2.0","id":"128","method":"PlcProgram.Read","params":{"var":"\"M_PRG_3\""}},
    # {"jsonrpc":"2.0","id":"129","method":"PlcProgram.Read","params":{"var":"\"M_PRG_4\""}},
    # {"jsonrpc":"2.0","id":"130","method":"PlcProgram.Read","params":{"var":"\"M_PRG_5\""}},
    # {"jsonrpc":"2.0","id":"131","method":"PlcProgram.Read","params":{"var":"\"M_PRG_6\""}},
    # {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"M_PRG_7\""}},
    # {"jsonrpc":"2.0","id":"133","method":"PlcProgram.Read","params":{"var":"\"gen\""}},
    {"jsonrpc":"2.0","id":"133","method":"PlcProgram.Read","params":{"var":"\"mar\".palabra"}}
    ])


    headers = {
        'X-Auth-Token': PLC_TOKEN['token'],
        'Content-Type': 'application/json',
        # 'verify': False
    }

    conn.request("POST", "/api/jsonrpc", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data_json = data.decode("utf-8")
    data_parsed = json.loads(data_json)
    # sensor_value = data_parsed["result"]
    # print(f"El valor que trae del plc es {sensor_value}")
    print("la data:", data_parsed)

def obtain_token_plc():
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    print("los threads activos son",threading.active_count())

    # frontState.led_on = True
    try:
        conn = http.client.HTTPSConnection("192.168.3.150")
    except:
        print("Conexion con plc no establecida")

    payload = json.dumps({
        "id": 0,
        "jsonrpc": "2.0",
        "method": "Api.Login",
        "params": {
            "user": "user",
            "password": "1234"
        }
    })
    headers = {
        # 'X-Auth-Token': 'hIcxhbH707fE+rKa0nzgfTu1azYu',
        'Content-Type': 'application/json',
    }
    conn.request("POST", "/api/jsonrpc", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data_json = data.decode("utf-8")
    data_parsed = json.loads(data_json)
    PLC_TOKEN['token'] = data_parsed["result"]["token"]
    print("el token es",PLC_TOKEN['token'])
    # print(data_parsed["result"]["token"])
def sensores_states_plc():
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    # lista con valores de los sensores
    DERIVED_SENSOR_STATES = []
    # vars para armar mensaje
    msg_data_directions_container = []
    first = '\"'
    last = '\"'

    try:
        conn = http.client.HTTPSConnection("192.168.3.150")
    except:
        print("Conexion con plc no establecida")    
    
    #arma el mensaje
    for n in range(0,len(LIST_OF_DIRECTIONS)):
        msg_data_directions = {"jsonrpc":"2.0","id":n,"method":"PlcProgram.Read","params":{"var":(first+LIST_OF_DIRECTIONS[n]+last)}}
        # print(msg_data_directions)
        msg_data_directions_container.append(msg_data_directions)

    #mensaje armado
    payload = json.dumps(msg_data_directions_container)

    headers = {
        'X-Auth-Token': control_vars.PLC_TOKEN['token'],
        'Content-Type': 'application/json',
    }

    #se manda el mensaje
    conn.request("POST", "/api/jsonrpc", payload, headers)

    #respuesata mensaje
    res = conn.getresponse()
    data = res.read()
    data_json = data.decode("utf-8")
    data_parsed = json.loads(data_json)
    count = 0
    for n in range(0, len(PLC_DEFAULT_VARIABLES)):
        bool_state_sensor = data_parsed[n]["result"]
        # print(bool_state_sensor)
        count += 1
        #append de los valores a la lista
        DERIVED_SENSOR_STATES.append(bool_state_sensor)
    # print(DERIVED_SENSOR_STATES)
    # print(count)
    # print(f"El valor que trae del plc es{bool_state_sensor}")
    return DERIVED_SENSOR_STATES

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
#         time.sleep(0.5)
#         while 1:
#             obtain_token_plc()
#             derived_sensores_states(sensores_plc())
#             data = {
#                 'mesa_armado_1' : int(param_vars.PARAMS['mesa_armado_1']),
#                 'mesa_armado_2' : int(param_vars.PARAMS['mesa_armado_2']),
#                 'okuma_1' : int(param_vars.PARAMS['okuma_1']),
#                 'okuma_2' : int(param_vars.PARAMS['okuma_2']),
#                 'okuma_3' : int(param_vars.PARAMS['okuma_3']),
#                 'okuma_4' : int(param_vars.PARAMS['okuma_4']),
#                 # 'mensajes_log': ws_vars.frontState.log_messages,
#                 'signal_0': int(control_vars.PLC_DEFAULT_VARIABLES['signal_0']),
#                 'signal_1': int(control_vars.PLC_DEFAULT_VARIABLES['signal_1']),
#                 'signal_2': int(control_vars.PLC_DEFAULT_VARIABLES['signal_2']),
#                 'signal_3': int(control_vars.PLC_DEFAULT_VARIABLES['signal_3']),
#                 'signal_4': int(control_vars.PLC_DEFAULT_VARIABLES['signal_4']),
#                 'signal_5': int(control_vars.PLC_DEFAULT_VARIABLES['signal_5']),
#                 'signal_6': int(control_vars.PLC_DEFAULT_VARIABLES['signal_6']),
#                 'signal_7': int(control_vars.PLC_DEFAULT_VARIABLES['signal_7']),
#                 'signal_8': int(control_vars.PLC_DEFAULT_VARIABLES['signal_8']),
#                 'signal_9': int(control_vars.PLC_DEFAULT_VARIABLES['signal_9']),
#             }
#             send_front_message(data)
#             time.sleep(0.5)


# class FrontWs(threading.Thread):

#     def __init__(self, **kwargs):
#         super(FrontWs, self).__init__(**kwargs)
    
#     def run(self):
#         while True:
#             time.sleep(3)
#             obtain_token_plc()


def threadA(dqu,):
    while True:
        # print(dqu)
        # print("entra al while")
        obtain_token_plc()
        time.sleep(120)





# class FrontWs():
#     start_service()
#     # send_front_message(data)
#     time.sleep(3)
