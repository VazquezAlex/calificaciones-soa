from django.shortcuts import render
from .models import ListaCalificacion

# Create your views here.
def index(request):
    calificaciones = ListaCalificacion.objects.all()

    return render(request, 'index.html', {"calificaciones": calificaciones})
    

def add(request):

    nombre = request.POST["nombre"]
    nombre_materia = request.POST["materia"]

    cal1 = int(request.POST["cal1"])
    cal2 = int(request.POST["cal2"])
    cal3 = int(request.POST["cal3"])

    prom = ((cal1 + cal2 + cal3)/3)

    c = ListaCalificacion.objects.create(
        alumno = nombre,
        materia = nombre_materia,
        calificacion1 = cal1,
        calificacion2 = cal2,
        calificacion3 = cal3,
        promedio = prom
    )

    return render(request, "lista.html", { "promedio" : prom, "nombre" : nombre }) 