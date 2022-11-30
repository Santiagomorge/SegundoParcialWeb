from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Aspirante
from .forms import CrearNuevoAspirante
# Create your views here.

def ListarAspirantes(request):
    aspirantes = list(Aspirante.objects.values()) 
    return JsonResponse(aspirantes, safe = False)


def aspiranteBD(request):
    
    aspirantes = Aspirante.objects.all()
    context = ({'aspirantes': aspirantes })
    return render(request, 'ver_aspirantes.html', context)

def CrearAspirante(request):
    if request.method == 'GET':
        return render(request, 'registrar_aspirantes.html',{
        'form': CrearNuevoAspirante()
        })
    else:
        Aspirante.objects.create(tipoDocumento = request.POST['tipoDocumento'], 
        numeroDocumento = request.POST['numeroDocumento'], nombre = request.POST['nombre'], 
        apellido = request.POST['apellido'], profesion = request.POST['profesion'], 
        edad = request.POST['edad'], ciudad = request.POST['ciudad'])
        return redirect('/aplicacion/')
    