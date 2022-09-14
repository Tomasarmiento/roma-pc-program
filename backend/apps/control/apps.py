from django.apps import AppConfig
# import django
from apps.control.utils import functions
from apps.ws.utils.functions import send_front_message
import time

import threading
from collections import deque
import asyncio

from apps.parameters.utils import variables



class ControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.control'

    def ready(self) -> None:
        print('start')
        # functions.obtain_token_plc()

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