from django.apps import AppConfig
from .api.service import start_service
from apps.ws.utils.functions import send_front_message
data = {
        'mesa_armado_1' : 2,
        'mesa_armado_2' : 1,
    }


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.service'

    # def ready(self):
    #     send_front_message(data)
    #     start_service()
    #     # listen()