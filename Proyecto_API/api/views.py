from django.http.response  import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Aspirante

# Create your views here
def aspirante(request):
    aspirantes = Aspirante.objects.all()
    context = ({'aspirantes': aspirantes})
    return render(request, 'templates/aspirantes.html', context)

def crear_aspirante(request):
    return render(request, 'templates/crear_aspirante.html')