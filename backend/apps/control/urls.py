from django.urls import path, re_path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('test-led/on/', views.switch_led_state_on, name='led-on'),
    path('test-led/off/', views.switch_led_state_off, name='led-off'),
    path('sensores/okuma/', views.sensores_okuma_identify, name='okuma'),
    path('sensores/mesa/', views.sensores_mesa_identify, name='mesa'),
]