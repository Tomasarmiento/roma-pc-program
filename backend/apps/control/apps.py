from django.apps import AppConfig
# import django
# from apps.control.utils import functions

class ControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.control'

    # def ready(self) -> None:
        # django.setup()
        # functions.FrontWs().start()