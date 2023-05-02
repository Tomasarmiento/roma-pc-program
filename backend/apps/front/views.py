from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, "index.html")

def hash1(request):
    return render(request, "hash1.html")

def neumatic_index(request):
    return render(request, "neumatic_index.html")

def okuma_1_neumatic(request):
    return render(request, "okuma_1_neumatic.html")

def okuma_2_neumatic(request):
    return render(request, "okuma_2_neumatic.html")

def okuma_3_neumatic(request):
    return render(request, "okuma_3_neumatic.html")

def okuma_4_neumatic(request):
    return render(request, "okuma_4_neumatic.html")

def mesa_1_neumatic(request):
    return render(request, "mesa_1_neumatic.html")

def mesa_2_neumatic(request):
    return render(request, "mesa_2_neumatic.html")

def gripper_neumatic(request):
    return render(request, "gripper_neumatic.html")

def semiAutomatico(request):
    return render(request, "mesa_1_semiAutomatico.html")

def automatico(request):
    return render(request, "automatico.html")

def error(request):
    return render(request, "error.html")

def desactivar_okuma(request):
    return render(request, "desactivar_okuma.html")

def instructivo(request):
    return render(request, "instructivo.html")