from apps.ws.utils.functions import send_front_message
from apps.ws.utils.variables import frontState
from apps.parameters.utils import variables as param_vars
import threading
import random, time
import json
from apps.service.api.service import start_service

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
