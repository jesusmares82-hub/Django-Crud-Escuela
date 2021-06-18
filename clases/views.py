from django.shortcuts import render

from clases.models import Clase


def clases(request):
    context = {}

    if request.method == 'GET':
        clases = Clase.objects.all()
        context = {
            "clases": clases
        }

    if request.method == 'POST':
        nueva_clase = {
            'nombre': request.POST['nombre'],
            'profesor': request.POST['profesor'],
            'dias_clase': request.POST['dias_clase'],
            'hora_inicio': request.POST['hora_inicio'],
            'hora_fin': request.POST['hora_fin']
        }
        Clase.objects.create(**nueva_clase)

        clases = Clase.objects.all()
        context = {
            "clases": clases,
            'message': 'La clase se ha creado satisfactoriamente!'
        }

    return render(request, 'clases/clases_disponibles.html', context)


def get_clase(request, clase_id):
    try:
        clase = Clase.objects.get(pk=clase_id)
        context = {
            "clase": clase
        }
        return render(request, 'clases/clases_detalle.html', context)
    except Exception as e:
        return render(request, 'clases/clases_detalle.html', {})


