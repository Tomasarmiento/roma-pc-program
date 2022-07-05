from django.urls import re_path

from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/front/', consumers.FrontConsumer.as_asgi()),               # ws://localhost:8000/ws/front/
]