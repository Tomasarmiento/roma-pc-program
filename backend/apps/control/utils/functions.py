from apps.ws.utils.functions import send_front_message
from apps.ws.utils.variables import frontState
import threading
import random, time

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
        while 1:
            data = {
                'husillo_rpm': float(random.randint(1,10)),
                'husillo_torque': float(random.randint(1,10)),

                'cabezal_pos': float(random.randint(-10,10)),
                'cabezal_vel': float(random.randint(1,10)),

                'avance_pos': float(random.randint(1,10)),
                'avance_vel': float(random.randint(1,10)),

                'led_state': frontState.led_on
            }
            send_front_message(data)
            time.sleep(1)