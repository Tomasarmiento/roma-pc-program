from asyncio import sleep
import threading
import time
from datetime import datetime

from apps.ws.utils.functions import send_front_message

from apps.control.utils import functions as ctrl_fun
from apps.control.utils import variables as ctrl_vars


class RoutineHandler(threading.Thread):

    def __init__(self, **kwargs):
        super(RoutineHandler, self).__init__(**kwargs)
        self.init_condition_checked = False
        self.enter_routine = 0
        self._stop_event = threading.Event()


    def run(self):
        while True:
            self.init_condition_checked = False
            if ctrl_vars.PLC_DEFAULT_VARIABLES["R_I_HF"] == True:
                if ctrl_vars.PLC_DEFAULT_VARIABLES[".pause_auto"] == False and ctrl_vars.PLC_DEFAULT_VARIABLES[".last_auto"] == False and ctrl_vars.PLC_DEFAULT_VARIABLES[".init_error"] == False:
                    self.init_condition_checked = True
                    self.enter_routine += 1
            else:
                self.init_condition_checked = False


            if self.init_condition_checked == True and self.enter_routine > 1:
                ctrl_fun.auto_change_drawer()
                time.sleep(2)

            time.sleep(2)
