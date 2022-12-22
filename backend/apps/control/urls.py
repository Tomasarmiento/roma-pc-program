from django.urls import path, re_path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('test-led/on/', views.switch_led_state_on, name='led-on'),
    path('test-led/off/', views.switch_led_state_off, name='led-off'),
    path('sensores/okuma/', views.sensores_okuma_identify, name='okuma'),
    path('sensores/mesa/', views.sensores_mesa_identify, name='mesa'),
    path('automatico/okuma/', views.disable_okuma, name='okuma'),
    path('automatico/buttons-cmd/', views.cmd_automatic_routines, name='cmd_automatic_routines'),
    path('disable_okuma/', views.cmd_disable_okuma, name='cmd_disable_okuma'),
    path('sensores/', views.ManualPneumatic.as_view(), name='manual-pneumatic'),
    path('semiautomatico/routine/', views.send_command_bit, name='semiAutomatico-routine'),
    path('msge-test/', views.msge_test, name='msge_test'),
    path('index_change/', views.index_change, name="index_change"),
    # path('ws/front/', views.switch_led_state_off, name='led-off'),
    # path('https://192.168.3.150/api/jsonrpc', views.token_register, name='okuma'),
]