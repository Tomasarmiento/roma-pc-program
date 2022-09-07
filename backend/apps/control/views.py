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
from apps.control.utils.functions import derived_sensores_states,sensores_plc


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


@csrf_exempt
def switch_led_state_off(request):
    list = [False,False,False,False,False,True,True,True,True,True]
    # derived_sensores_states(sensores_plc())
    derived_sensores_states(list)
    return JsonResponse({})


# @csrf_exempt
# def switch_led_state_off(request):
#     import ssl
#     ssl._create_default_https_context = ssl._create_unverified_context
#     # frontState.led_on = True
#     DERIVED_SENSOR_STATES = []
#     conn = http.client.HTTPSConnection("192.168.3.150")
#     payload = json.dumps({
#         "id": 0,
#         "jsonrpc": "2.0",
#         "method": "PlcProgram.Read", #Write #Read
#         "params": {
#             "var": "\"mar\".markarray[0]",#array database
#             # "var": "\"OUT_13\"", #entrada salida modificar
#             # "value": False  #entrada salida modificar
#         }
#     })


#     headers = {
#         'X-Auth-Token': PLC_TOKEN['token'],
#         'Content-Type': 'application/json',
#     }

#     # conn.request("POST", "/api/jsonrpc", payload, headers)
#     # res = conn.getresponse()
#     # data = res.read()
#     # data_json = data.decode("utf-8")
#     # data_parsed = json.loads(data_json)
#     # print("la data:", data_parsed)

#     for n in range(0,len(DEFAULT_SENSOR_STATES)):
#         #cambia valor del json para obtener todos los valores de los sensores
#         strValue = payload
#         strToReplace   = '0'
#         replacementStr = str(n)
#         strValue = replacementStr.join(strValue.rsplit(strToReplace, 1))
#         # print(strValue)


#         #se manda el mensaje
#         conn.request("POST", "/api/jsonrpc", strValue, headers)
#         res = conn.getresponse()
#         data = res.read()
#         data_json = data.decode("utf-8")
#         data_parsed = json.loads(data_json)
#         sensor_value = data_parsed["result"]
#         print(f"El valor que trae del plc es{sensor_value}")


#         DERIVED_SENSOR_STATES.append(sensor_value)
#         # list(PLC_DEFAULT_VARIABLES.keys())[0]
#         # list(PLC_DEFAULT_VARIABLES.keys())[8] = True
#         # print(PLC_DEFAULT_VARIABLES)
#     print(DERIVED_SENSOR_STATES)


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
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    # frontState.led_on = True
    conn = http.client.HTTPSConnection("192.168.3.150")
    payload = json.dumps({
        "id": 0,
        "jsonrpc": "2.0",
        "method": "Api.Login",
        "params": {
            "user": "user",
            "password": "asdf"
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