from django.shortcuts import render

from estudiantes.models import Estudiante


def estudiantes(request):
    context = {}

    if request.method == 'GET':
        estudiantes = Estudiante.objects.all()
        context = {
            "estudiantes": estudiantes
        }

    if request.method == 'POST':
        nuevo_estudiante = {
            'nombre': request.POST['nombre'],
            'edad': request.POST['edad'],
            'email': request.POST['email'],
            'fecha_nacimiento': request.POST['fecha_nacimiento']
        }
        Estudiante.objects.create(**nuevo_estudiante)

        estudiantes = Estudiante.objects.all()
        context = {
            "estudiantes": estudiantes,
            'message': 'El estudiante se se ha creado satisfactoriamente!'
        }

    return render(request, 'estudiantes/estudiantes_lista.html', context)


def get_estudiante(request, estudiante_id):
    try:
        estudiante = Estudiante.objects.get(pk=estudiante_id)
        context = {
            "estudiante": estudiante
        }
        return render(request, 'estudiantes/estudiantes_detalle.html', context)
    except Exception as e:
        return render(request, 'estudiantes/cestudiantes_detalle.html', {})



