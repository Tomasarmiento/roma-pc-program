from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('hash1/', views.hash1, name="hash1"),
    path('neumatic_index/', views.neumatic_index, name="neumatic_index"),
    path('manual/okuma_1_neumatic/', views.okuma_1_neumatic, name="okuma_1_neumatic"),
    path('manual/okuma_2_neumatic/', views.okuma_2_neumatic, name="okuma_2_neumatic"),
    path('manual/okuma_3_neumatic/', views.okuma_3_neumatic, name="okuma_3_neumatic"),
    path('manual/okuma_4_neumatic/', views.okuma_4_neumatic, name="okuma_4_neumatic"),
    path('manual/mesa_1_neumatic/', views.mesa_1_neumatic, name="mesa_1_neumatic"),
    path('manual/mesa_2_neumatic/', views.mesa_2_neumatic, name="mesa_2_neumatic"),
    path('manual/gripper_neumatic/', views.gripper_neumatic, name="gripper_neumatic"),
    path('semiAutomatico/', views.semiAutomatico, name="semiAutomatico"),
    path('automatico/', views.automatico, name="automatico"),

]