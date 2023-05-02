from apps.ws.utils.functions import send_front_message
from apps.ws.utils.variables import frontState
from apps.parameters.utils import variables as param_vars
import http.client
from apps.control.utils import variables as control_vars
import threading
import random, time
from datetime import datetime
import json
from apps.service.api.service import start_service
from apps.ws.utils import variables as ws_vars
from apps.service.api.protocols import OPCProtocol
from apps.ws.utils.variables import OPC_variables



from apps.control.utils.variables import PLC_TOKEN,LIST_OF_DIRECTIONS,PLC_DEFAULT_VARIABLES,MSG_ERROR_DIRECTIONS,MSG_ERROR_CODIFICATION,TAGS_DIRECTIONS

#append de leyenda de errores activos a lista que se manda por websocket
def update_msg_error(list_state_sensores):
    old_list_errors = ws_vars.frontState.log_messages.copy()
    # print(old_list_errors)

    ws_vars.frontState.log_messages = []
    for key, value in (list_state_sensores.items()):
        # print(key,value)
        if key in MSG_ERROR_DIRECTIONS:
            # print(value)
            # print("antes",ws_vars.frontState.log_messages)
           
            if value == True :  # and MSG_ERROR_CODIFICATION[key] not in ws_vars.frontState.log_messages
                # count += 1
                # print(MSG_ERROR_CODIFICATION[key])
                ws_vars.frontState.log_messages.append(MSG_ERROR_CODIFICATION[key])
            # print(ws_vars.frontState.log_messages)
            # else:
            #     ws_vars.frontState.log_messages.append("")
    for n in ws_vars.frontState.log_messages:
        if n not in old_list_errors:
            now_time = datetime.now()
            timestamp = now_time.strftime("%m/%d/%y %H:%M:%S")
            msg_value = n
            msg = timestamp + ' - ' + msg_value
            ws_vars.frontState.err_messages.append(msg)
    # print(ws_vars.frontState.err_messages)

#modifica diccionario local de sensores en false al valor en el que se encuentra actualmente
def derived_sensores_states(list_state_sensores):
    # print(len(list_state_sensores))
    # print(len(control_vars.PLC_DEFAULT_VARIABLES))
    # print(len(control_vars.LIST_OF_DIRECTIONS))
    
    for n in range(0,len(list_state_sensores)):
        for w in range(0,len(control_vars.PLC_DEFAULT_VARIABLES)):
            # print("primer len",len(list_state_sensores),"segundo len",len(control_vars.PLC_DEFAULT_VARIABLES))
            if n == w:
                control_vars.PLC_DEFAULT_VARIABLES[control_vars.LIST_OF_DIRECTIONS[w]] = list_state_sensores[n]
    # print(control_vars.PLC_DEFAULT_VARIABLES.values())
    return control_vars.PLC_DEFAULT_VARIABLES

#funcion para cambiar automaticamente los drawer al inciar rutina de robot(falta activar el thread master para que funcione)
def auto_change_drawer():
    OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_CG"',False)
    
    if (PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_1"] == True) and (PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_2"] == True) and (PLC_DEFAULT_VARIABLES["MA1_I_DR_D_NS"] == True):
        OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_DRU_FD"',False)
        OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_DRD_FD"',True)
        time.sleep(5)
        if PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_1"] == False and PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_2"] == False and PLC_DEFAULT_VARIABLES["MA1_I_DR_D_NS"] == False:
            OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_CG"',True)

    elif PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_1"] == False and PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_2"] == False and PLC_DEFAULT_VARIABLES["MA1_I_DR_D_NS"] == False:
        OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_DRU_FD"',True)
        OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_DRD_FD"',False)
        time.sleep(5)
        print(PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_1"],PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_2"],PLC_DEFAULT_VARIABLES["MA1_I_DR_D_NS"])

        if PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_1"] == True and PLC_DEFAULT_VARIABLES["MA1_I_DR_U_ES_2"] == True and PLC_DEFAULT_VARIABLES["MA1_I_DR_D_NS"] == False:
            OPCProtocol().write_value_bool('ns=3;s="tags"."Man_MA1_CG"',True)

#peticion de token login al plc
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

#funcion para pedir arrays de ints(routine steps)
def update_step_routine():
    OPCProtocol().read_input_value('ns=3;s="tags"."ints"', False) #poner ruta del array step

#thread para pedir array con valor de sensores y mandar al front(se inicia en apps)
class FrontWs(threading.Thread):

    def __init__(self, **kwargs):
        super(FrontWs, self).__init__(**kwargs)
        
    
    def run(self):
        while True:
            inicio = time.time()
            if ws_vars.WEBSOCKET == True:

                # OPCProtocol().read_input_value('ns=3;s="tags"."data"', True)
                # update_step_routine()
                
                data = {
                    # 'mesa_armado_1' : int(param_vars.PARAMS['mesa_armado_1']),
                    # 'mesa_armado_2' : int(param_vars.PARAMS['mesa_armado_2']),
                    # 'okuma_1' : int(param_vars.PARAMS['okuma_1']),
                    # 'okuma_2' : int(param_vars.PARAMS['okuma_2']),
                    # 'okuma_3' : int(param_vars.PARAMS['okuma_3']),
                    # 'okuma_4' : int(param_vars.PARAMS['okuma_4']),
                    'mensajes_log': ws_vars.frontState.log_messages,
                    'plc_sensors': control_vars.PLC_DEFAULT_VARIABLES,
                    'plc_int_variables':  control_vars.PLC_DEFAULT_VARIABLES_INT,
                    'mensajes_error_log': ws_vars.frontState.err_messages,
                }

                send_front_message(data)

                time.sleep(OPC_variables.REFRESH_TIME)
            # delta = time.time() - inicio
            # print("el delta es",delta)
