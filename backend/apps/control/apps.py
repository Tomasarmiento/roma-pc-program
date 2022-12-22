from django.apps import AppConfig
# import django
from apps.control.utils import functions
from apps.ws.utils.functions import send_front_message
from apps.control.utils.variables import LIST_OF_DIRECTIONS,PLC_DEFAULT_VARIABLES
import time
from opcua import Client, ua

import threading
from collections import deque
import asyncio

from apps.ws.utils import variables as ws_vars
from apps.parameters.utils import variables
from apps.ws.utils.variables import OPC_variables
from apps.control.utils.routines import RoutineHandler




class ControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.control'
    

    def ready(self) -> None:
        print('start')
        OPC_variables.CLIENT.connect()
        ws_vars.WEBSOCKET = True
        # functions.obtain_token_plc()
        functions.FrontWs().start()
        # RoutineHandler().start()


    # def ready(self) -> None:
    #     start_thread = True


 
        # if start_thread == True:
        #     dequeAB = deque()
        #     readThread = threading.Thread(target=functions.threadA, args=(dequeAB,), daemon=True)
        #     print("dentro de ready")
        #     try:
        #         readThread.start()
        #         variables.count += 1
        #         start_thread = False
        #     except (KeyboardInterrupt, SystemExit):
        #         print("except")
        #         readThread.join()
        # print("------------")
        # print("------------")
        # print("el count es",variables.count)
        # functions.FrontWs().start()
        # functions.FrontWs()