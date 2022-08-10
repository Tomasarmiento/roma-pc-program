from apps.ws.utils.functions import send_front_message
from apps.ws.utils.variables import frontState
from apps.parameters.utils import variables as param_vars
import threading
import random, time
import json
from django.core.serializers.json import DjangoJSONEncoder

# def get_front_states():
#     data = {'hola':10}
#     return data

# data = get_front_states()
# send_front_message(data)
# print("hola")


class FrontWs(threading.Thread):

    def __init__(self, **kwargs):
        super(FrontWs, self).__init__(**kwargs)
    
    def run(self):
        time.sleep(3)
        while 1:
            data = {
                'okuma_1' : param_vars.PARAMS['okuma_1'],
                'okuma_2' : param_vars.PARAMS['okuma_2'],
                'okuma_3' : param_vars.PARAMS['okuma_3'],
                'okuma_4' : param_vars.PARAMS['okuma_4'],
                'led_state': frontState.led_on,
            }
            send_front_message(json.dumps((data), cls=DjangoJSONEncoder))
            time.sleep(3)