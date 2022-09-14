import json
import http.client
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect



from apps.ws.utils.functions import send_front_message
from apps.ws.utils.variables import frontState

from apps.parameters.utils.functions import toggle_disable_machine
from apps.parameters.models import Parameter

from apps.control.utils.variables import OKUMA,MESA,PLC_TOKEN,PLC_DEFAULT_VARIABLES,PLC_VARIABLES,DEFAULT_SENSOR_STATES
from apps.control.utils.functions import derived_sensores_states,sensores_plc,obtain_token_plc


@csrf_exempt
def token_register(request):
    msg = 'hello world'
    frontState.log_messages.append(msg)
    print()


# @csrf_exempt
# def token_register(request):
#     {
#     "id": 0,
#     "jsonrpc": "2.0",
#     "method": "Api.Login",
#     "params": {
#         "user": "user",
#         "password": "1234"
#     }
# }

@csrf_exempt
def disable_okuma(request):
    post_req = request.POST
    model_machine = post_req['model_machine']
    model_machine2 = str(model_machine)
    # print("el request es:",request.POST)
    toggle_disable_machine(model_machine2)
    # data = {
    #         'mesa_armado_1' : 1,
    #         'mesa_armado_2' : 0,
    #         }
    # send_front_message(data)
    print("enter to button")
    
    return JsonResponse({})

json_send = {
    "id": 0,
    "jsonrpc": "2.0",
    "method": "PlcProgram.Read",
    "params": {
        "var": "\"mar\".markarray[3]",
    }
}
# @csrf_exempt
# def switch_led_state_off(request):
#     list = [False,False,False,False,False,True,True,True,True,True]
#     # derived_sensores_states(sensores_plc())
#     derived_sensores_states(list)
#     return JsonResponse({})

@csrf_exempt
def switch_led_state_off(request):
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    conn = http.client.HTTPSConnection("192.168.3.150")
    payload = json.dumps([
    {"jsonrpc":"2.0","id":"1","method":"PlcProgram.Read","params":{"var":"\"CH1_I_RA\""}},
    {"jsonrpc":"2.0","id":"2","method":"PlcProgram.Read","params":{"var":"\"CH1_I_AL\""}},
    {"jsonrpc":"2.0","id":"3","method":"PlcProgram.Read","params":{"var":"\"CH1_I_ID\""}},
    {"jsonrpc":"2.0","id":"4","method":"PlcProgram.Read","params":{"var":"\"CH1_I_MB\""}},
    {"jsonrpc":"2.0","id":"5","method":"PlcProgram.Read","params":{"var":"\"CH1_I_PS\""}},
    {"jsonrpc":"2.0","id":"6","method":"PlcProgram.Read","params":{"var":"\"CH1_I_HO\""}},
    {"jsonrpc":"2.0","id":"7","method":"PlcProgram.Read","params":{"var":"\"CH1_I_NPA\""}},
    {"jsonrpc":"2.0","id":"8","method":"PlcProgram.Read","params":{"var":"\"CH1_I_NPR\""}},
    {"jsonrpc":"2.0","id":"9","method":"PlcProgram.Read","params":{"var":"\"CH2_I_RA\""}},
    {"jsonrpc":"2.0","id":"10","method":"PlcProgram.Read","params":{"var":"\"CH2_I_AL\""}},
    {"jsonrpc":"2.0","id":"11","method":"PlcProgram.Read","params":{"var":"\"CH2_I_ID\""}},
    {"jsonrpc":"2.0","id":"12","method":"PlcProgram.Read","params":{"var":"\"CH2_I_MB\""}},
    {"jsonrpc":"2.0","id":"13","method":"PlcProgram.Read","params":{"var":"\"CH2_I_PS\""}},
    {"jsonrpc":"2.0","id":"14","method":"PlcProgram.Read","params":{"var":"\"CH2_I_HO\""}},
    {"jsonrpc":"2.0","id":"15","method":"PlcProgram.Read","params":{"var":"\"CH2_I_NPA\""}},
    {"jsonrpc":"2.0","id":"16","method":"PlcProgram.Read","params":{"var":"\"CH2_I_NPR\""}},
    {"jsonrpc":"2.0","id":"17","method":"PlcProgram.Read","params":{"var":"\"CH3_I_RA\""}},
    {"jsonrpc":"2.0","id":"18","method":"PlcProgram.Read","params":{"var":"\"CH3_I_AL\""}},
    {"jsonrpc":"2.0","id":"19","method":"PlcProgram.Read","params":{"var":"\"CH3_I_ID\""}},
    {"jsonrpc":"2.0","id":"20","method":"PlcProgram.Read","params":{"var":"\"CH3_I_MB\""}},
    {"jsonrpc":"2.0","id":"21","method":"PlcProgram.Read","params":{"var":"\"CH3_I_PS\""}},
    {"jsonrpc":"2.0","id":"22","method":"PlcProgram.Read","params":{"var":"\"CH3_I_HO\""}},
    {"jsonrpc":"2.0","id":"23","method":"PlcProgram.Read","params":{"var":"\"CH3_I_NPA\""}},
    {"jsonrpc":"2.0","id":"24","method":"PlcProgram.Read","params":{"var":"\"CH3_I_NPR\""}},
    {"jsonrpc":"2.0","id":"25","method":"PlcProgram.Read","params":{"var":"\"CH4_I_RA\""}},
    {"jsonrpc":"2.0","id":"26","method":"PlcProgram.Read","params":{"var":"\"CH4_I_AL\""}},
    {"jsonrpc":"2.0","id":"27","method":"PlcProgram.Read","params":{"var":"\"CH4_I_ID\""}},
    {"jsonrpc":"2.0","id":"28","method":"PlcProgram.Read","params":{"var":"\"CH4_I_MB\""}},
    {"jsonrpc":"2.0","id":"29","method":"PlcProgram.Read","params":{"var":"\"CH4_I_PS\""}},
    {"jsonrpc":"2.0","id":"30","method":"PlcProgram.Read","params":{"var":"\"CH4_I_HO\""}},
    {"jsonrpc":"2.0","id":"31","method":"PlcProgram.Read","params":{"var":"\"CH4_I_NPA\""}},
    {"jsonrpc":"2.0","id":"32","method":"PlcProgram.Read","params":{"var":"\"CH4_I_NPR\""}},
    {"jsonrpc":"2.0","id":"33","method":"PlcProgram.Read","params":{"var":"\"R_I_AL\""}},
    {"jsonrpc":"2.0","id":"34","method":"PlcProgram.Read","params":{"var":"\"R_I_HF\""}},
    {"jsonrpc":"2.0","id":"35","method":"PlcProgram.Read","params":{"var":"\"R_I_ID\""}},
    {"jsonrpc":"2.0","id":"36","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_0\""}},
    {"jsonrpc":"2.0","id":"37","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_1\""}},
    {"jsonrpc":"2.0","id":"38","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_2\""}},
    {"jsonrpc":"2.0","id":"39","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_3\""}},
    {"jsonrpc":"2.0","id":"40","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_4\""}},
    {"jsonrpc":"2.0","id":"41","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_5\""}},
    {"jsonrpc":"2.0","id":"42","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_6\""}},
    {"jsonrpc":"2.0","id":"43","method":"PlcProgram.Read","params":{"var":"\"R_I_PRG_7\""}},
    {"jsonrpc":"2.0","id":"44","method":"PlcProgram.Read","params":{"var":"\"R_I_G1_PS\""}},
    {"jsonrpc":"2.0","id":"45","method":"PlcProgram.Read","params":{"var":"\"R_I_G2_PS\""}},
    {"jsonrpc":"2.0","id":"46","method":"PlcProgram.Read","params":{"var":"\"R_I_FLS\""}},
    {"jsonrpc":"2.0","id":"47","method":"PlcProgram.Read","params":{"var":"\"R_I_RLS\""}},
    {"jsonrpc":"2.0","id":"48","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_PS_1\""}},
    {"jsonrpc":"2.0","id":"49","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_PS_2\""}},
    {"jsonrpc":"2.0","id":"50","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_PS_1\""}},
    {"jsonrpc":"2.0","id":"51","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_PS_2\""}},
    {"jsonrpc":"2.0","id":"52","method":"PlcProgram.Read","params":{"var":"\"MA1_I_GS_UP\""}},
    {"jsonrpc":"2.0","id":"53","method":"PlcProgram.Read","params":{"var":"\"MA1_I_GS_DN\""}},
    {"jsonrpc":"2.0","id":"54","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_ES_1\""}},
    {"jsonrpc":"2.0","id":"55","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_ES_2\""}},
    {"jsonrpc":"2.0","id":"56","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_ES_1\""}},
    {"jsonrpc":"2.0","id":"57","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_ES_2\""}},
    {"jsonrpc":"2.0","id":"58","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_NS\""}},
    {"jsonrpc":"2.0","id":"59","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_NS\""}},
    {"jsonrpc":"2.0","id":"60","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_1_SA\""}},
    {"jsonrpc":"2.0","id":"61","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_1_SR\""}},
    {"jsonrpc":"2.0","id":"62","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_2_SA\""}},
    {"jsonrpc":"2.0","id":"63","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_U_BP_2_SR\""}},
    {"jsonrpc":"2.0","id":"64","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_1_SA\""}},
    {"jsonrpc":"2.0","id":"65","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_1_SR\""}},
    {"jsonrpc":"2.0","id":"66","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_2_SA\""}},
    {"jsonrpc":"2.0","id":"67","method":"PlcProgram.Read","params":{"var":"\"MA1_I_DR_D_BP_2_SR\""}},
    {"jsonrpc":"2.0","id":"68","method":"PlcProgram.Read","params":{"var":"\"MA1_I_OB\""}},
    {"jsonrpc":"2.0","id":"69","method":"PlcProgram.Read","params":{"var":"\"MA1_I_EMS\""}},
    {"jsonrpc":"2.0","id":"70","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_PS_1\""}},
    {"jsonrpc":"2.0","id":"71","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_PS_2\""}},
    {"jsonrpc":"2.0","id":"72","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_PS_1\""}},
    {"jsonrpc":"2.0","id":"73","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_PS_2\""}},
    {"jsonrpc":"2.0","id":"74","method":"PlcProgram.Read","params":{"var":"\"MA2_I_GS_UP\""}},
    {"jsonrpc":"2.0","id":"75","method":"PlcProgram.Read","params":{"var":"\"MA2_I_GS_DN\""}},
    {"jsonrpc":"2.0","id":"76","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_ES_1\""}},
    {"jsonrpc":"2.0","id":"77","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_ES_2\""}},
    {"jsonrpc":"2.0","id":"78","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_ES_1\""}},
    {"jsonrpc":"2.0","id":"79","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_ES_2\""}},
    {"jsonrpc":"2.0","id":"80","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_NS\""}},
    {"jsonrpc":"2.0","id":"81","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_NS\""}},
    {"jsonrpc":"2.0","id":"82","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_1_SA\""}},
    {"jsonrpc":"2.0","id":"83","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_1_SR\""}},
    {"jsonrpc":"2.0","id":"84","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_2_SA\""}},
    {"jsonrpc":"2.0","id":"85","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_U_BP_2_SR\""}},
    {"jsonrpc":"2.0","id":"86","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_1_SA\""}},
    {"jsonrpc":"2.0","id":"87","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_1_SR\""}},
    {"jsonrpc":"2.0","id":"88","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_2_SA\""}},
    {"jsonrpc":"2.0","id":"89","method":"PlcProgram.Read","params":{"var":"\"MA2_I_DR_D_BP_2_SR\""}},
    {"jsonrpc":"2.0","id":"90","method":"PlcProgram.Read","params":{"var":"\"MA2_I_OB\""}},
    {"jsonrpc":"2.0","id":"91","method":"PlcProgram.Read","params":{"var":"\"MA2_I_EMS\""}},
    {"jsonrpc":"2.0","id":"92","method":"PlcProgram.Read","params":{"var":"\"GRL_I_EMS\""}},
    {"jsonrpc":"2.0","id":"93","method":"PlcProgram.Read","params":{"var":"\"System_Active\""}},
    {"jsonrpc":"2.0","id":"94","method":"PlcProgram.Read","params":{"var":"\"Start_system_button\""}},
    {"jsonrpc":"2.0","id":"95","method":"PlcProgram.Read","params":{"var":"\"Stop_system_button\""}},
    {"jsonrpc":"2.0","id":"96","method":"PlcProgram.Read","params":{"var":"\"Emergency\""}},
    {"jsonrpc":"2.0","id":"97","method":"PlcProgram.Read","params":{"var":"\"Robot_GO\""}},
    {"jsonrpc":"2.0","id":"98","method":"PlcProgram.Read","params":{"var":"\"Robot_IDLE\""}},
    {"jsonrpc":"2.0","id":"99","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRU1\""}},
    {"jsonrpc":"2.0","id":"100","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_1_OP40\""}},
    {"jsonrpc":"2.0","id":"101","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRU2\""}},
    {"jsonrpc":"2.0","id":"102","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_2_OP40\""}},
    {"jsonrpc":"2.0","id":"103","method":"PlcProgram.Read","params":{"var":"\"Gen_Program\""}},
    {"jsonrpc":"2.0","id":"104","method":"PlcProgram.Read","params":{"var":"\"unblock_pallet\""}},
    {"jsonrpc":"2.0","id":"105","method":"PlcProgram.Read","params":{"var":"\"unblocked_pallet_sensor\""}},
    {"jsonrpc":"2.0","id":"106","method":"PlcProgram.Read","params":{"var":"\"neumatic_forward\""}},
    {"jsonrpc":"2.0","id":"107","method":"PlcProgram.Read","params":{"var":"\"neumatic_advance\""}},
    {"jsonrpc":"2.0","id":"108","method":"PlcProgram.Read","params":{"var":"\"INF30\""}},
    {"jsonrpc":"2.0","id":"109","method":"PlcProgram.Read","params":{"var":"\"Blower\""}},
    {"jsonrpc":"2.0","id":"110","method":"PlcProgram.Read","params":{"var":"\"Booster\""}},
    {"jsonrpc":"2.0","id":"111","method":"PlcProgram.Read","params":{"var":"\"INF40\""}},
    {"jsonrpc":"2.0","id":"112","method":"PlcProgram.Read","params":{"var":"\"pallet_sensor\""}},
    {"jsonrpc":"2.0","id":"113","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_1_OP20\""}},
    {"jsonrpc":"2.0","id":"114","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_2_OP20\""}},
    {"jsonrpc":"2.0","id":"115","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_1_OP20\""}},
    {"jsonrpc":"2.0","id":"116","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_U_2_OP20\""}},
    {"jsonrpc":"2.0","id":"117","method":"PlcProgram.Read","params":{"var":"\"OP20_available\""}},
    {"jsonrpc":"2.0","id":"118","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRD1\""}},
    {"jsonrpc":"2.0","id":"119","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_2_OP40\""}},
    {"jsonrpc":"2.0","id":"120","method":"PlcProgram.Read","params":{"var":"\"Trig_MA1DRD2\""}},
    {"jsonrpc":"2.0","id":"121","method":"PlcProgram.Read","params":{"var":"\"MA1_DR_D_1_OP40\""}},
    {"jsonrpc":"2.0","id":"122","method":"PlcProgram.Read","params":{"var":"\"R_I_MA1F\""}},
    {"jsonrpc":"2.0","id":"123","method":"PlcProgram.Read","params":{"var":"\"R_I_MA2F\""}},
    {"jsonrpc":"2.0","id":"124","method":"PlcProgram.Read","params":{"var":"\"okuma_available\""}},
    {"jsonrpc":"2.0","id":"125","method":"PlcProgram.Read","params":{"var":"\"M_PRG_0\""}},
    {"jsonrpc":"2.0","id":"126","method":"PlcProgram.Read","params":{"var":"\"M_PRG_1\""}},
    {"jsonrpc":"2.0","id":"127","method":"PlcProgram.Read","params":{"var":"\"M_PRG_2\""}},
    {"jsonrpc":"2.0","id":"128","method":"PlcProgram.Read","params":{"var":"\"M_PRG_3\""}},
    {"jsonrpc":"2.0","id":"129","method":"PlcProgram.Read","params":{"var":"\"M_PRG_4\""}},
    {"jsonrpc":"2.0","id":"130","method":"PlcProgram.Read","params":{"var":"\"M_PRG_5\""}},
    {"jsonrpc":"2.0","id":"131","method":"PlcProgram.Read","params":{"var":"\"M_PRG_6\""}},
    {"jsonrpc":"2.0","id":"132","method":"PlcProgram.Read","params":{"var":"\"M_PRG_7\""}},
    {"jsonrpc":"2.0","id":"133","method":"PlcProgram.Read","params":{"var":"\"gen\""}},
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

    return JsonResponse({})

# @csrf_exempt
# def switch_led_state_off(request):
#     import ssl
#     ssl._create_default_https_context = ssl._create_unverified_context
#     conn = http.client.HTTPSConnection("192.168.3.150")
#     payload = json.dumps({
#         "id": 0,
#         "jsonrpc": "2.0",
#         "method": "PlcProgram.Read", #Write #Read
#         "params": {
#             "var": "\"mar\".markarray[3]",#array database
#             # "var": "\"Emergency\"", #entrada salida modificar
#             # "value": True  #entrada salida modificar
#         }
#     })


#     headers = {
#         'X-Auth-Token': PLC_TOKEN['token'],
#         'Content-Type': 'application/json',
#         # 'verify': False
#     }

#     conn.request("POST", "/api/jsonrpc", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     data_json = data.decode("utf-8")
#     data_parsed = json.loads(data_json)
#     sensor_value = data_parsed["result"]
#     print(f"El valor que trae del plc es {sensor_value}")
#     # print("la data:", data_parsed)

#     # for n in range(0,len(DEFAULT_SENSOR_STATES)):
#     #     #cambia valor del json para obtener todos los valores de los sensores
#     #     strValue = payload
#     #     strToReplace   = '0'
#     #     replacementStr = str(n)
#     #     strValue = replacementStr.join(strValue.rsplit(strToReplace, 1))
#     #     # print(strValue)


#     #     #se manda el mensaje
#     #     conn.request("POST", "/api/jsonrpc", strValue, headers)
#     #     res = conn.getresponse()
#     #     data = res.read()
#     #     data_json = data.decode("utf-8")
#     #     data_parsed = json.loads(data_json)
#     #     sensor_value = data_parsed["result"]
#     #     print(f"El valor que trae del plc es{sensor_value}")


#     #     DERIVED_SENSOR_STATES.append(sensor_value)
#     #     # list(PLC_DEFAULT_VARIABLES.keys())[0]
#     #     # list(PLC_DEFAULT_VARIABLES.keys())[8] = True
#     #     # print(PLC_DEFAULT_VARIABLES)
#     # print(DERIVED_SENSOR_STATES)


#         # values_sensors(sensor_value)


#     # frontState.led_on = False
#     # params = Parameter.objects.all()
#     # contable = params.filter(machine_model=1).get(name='okuma_1')
#     # print(contable.value)
#     # msg = 'hello world'
#     # frontState.log_messages.append(msg)
#     # print()
#     # toggle_disable_machine('okuma_1',True)
#     return JsonResponse({})

@csrf_exempt
def switch_led_state_on(request):
    obtain_token_plc()

    return JsonResponse({})

@csrf_exempt
def sensores_okuma_identify(request):
    post_req = request.POST
    if post_req['model_machine']:
        okuma_model = str(post_req['model_machine'])
        okuma_especific_model = okuma_model[6]
        OKUMA['okuma_current_selected'] = int(okuma_especific_model)
        # if OKUMA['okuma_current_selected'] == 1:
        #     return HttpResponseRedirect(reverse('okuma_1_neumatic'))
        print(OKUMA['okuma_current_selected'])
        return JsonResponse({})


@csrf_exempt
def sensores_mesa_identify(request):
    post_req = request.POST
    print(post_req)
    if post_req['model_table']:
        mesa_model = str(post_req['model_table'])
        mesa_especific_model = mesa_model[5]
        MESA['mesa_current_selected'] = int(mesa_especific_model)
        # if OKUMA['okuma_current_selected'] == 1:
        #     return HttpResponseRedirect(reverse('okuma_1_neumatic'))
        print(MESA['mesa_current_selected'])
        return JsonResponse({})

# for n in range(0,5):
#         if n == okuma_especific_model:
#             print("dentro de if")
#             OKUMA['okuma_current_selected'] =  okuma_especific_model
#             print(OKUMA['okuma_current_selected'])
#             return render(request, "hash2.html", context={"name":"hash1.html"})
#             # return render(request, "index.html", context={"name":"hash1.html"})
#     # print(okuma_model[6])