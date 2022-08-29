from django.apps import AppConfig
# import django
# from apps.control.utils import functions
from apps.ws.utils.functions import send_front_message

data = {
        'mesa_armado_1' : 2,
        'mesa_armado_2' : 1,
    }

class ControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.control'

    # def ready(self) -> None:
    #     # send_front_message(data)
    #     # django.setup()
    #     # functions.FrontWs().start()
    #     functions.FrontWs()