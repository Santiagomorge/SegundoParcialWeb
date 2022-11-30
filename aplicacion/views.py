from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Aspirante, EvaluacionAdmision
from .forms import CrearNuevoAspirante
# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def notas(puntosHojaVida, puntosExperiencia, puntosPostgrados, puntosCertificaciones, puntosIngles):
    a = puntosHojaVida
    b = puntosExperiencia
    c = puntosPostgrados
    d = puntosCertificaciones
    e = puntosIngles
    result = a+b+c+d+e
    return HttpResponse ("<h2> Puntos del aspirante : %s</h2> " %result)

def listarnotas(request):
    evaluacionadmision = EvaluacionAdmision.objects.all()
    context = ({'evaluacionadmision': evaluacionadmision })
    return render(request, 'ver_notas.html', context)


def ListarAspirantes(request):
    aspirantes = list(Aspirante.objects.values()) 
    return JsonResponse(aspirantes, safe = False)

def listarEvaluaciones(request):
    evaluaciones = list(EvaluacionAdmision.objects.values())
    return JsonResponse(evaluaciones, safe = False)

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
