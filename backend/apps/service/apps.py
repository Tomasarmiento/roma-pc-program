from django.apps import AppConfig
from .api.service import start_service
from apps.ws.utils.functions import send_front_message
import time

from opcua import Client, ua
from apps.ws.utils.variables import OPC_variables


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.service'
    # client = Client(OPC_variables.URI+OPC_variables.HOST+OPC_variables.PORT)

    # def ready(self):
    #     time.sleep()
        
    #     OPC_variables.CLIENT.connect()
        # self.client.connect()
        # pass

    #     send_front_message(data)
    #     start_service()
    #     # listen()