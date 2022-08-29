import json
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

from apps.control.utils.variables import OKUMA,MESA

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
    # frontState.led_on = False
    # params = Parameter.objects.all()
    # contable = params.filter(machine_model=1).get(name='okuma_1')
    # print(contable.value)
    toggle_disable_machine('okuma_1',True)
    return JsonResponse({})

@csrf_exempt
def switch_led_state_on(request):
    frontState.led_on = True
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