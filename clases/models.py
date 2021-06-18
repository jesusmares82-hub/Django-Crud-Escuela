from django.db import models

from estudiantes.models import Estudiante


class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.CharField(max_length=50)
    dias_clase = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estudiantes = models.ManyToManyField(Estudiante, related_name='clases')

    def __str__(self):
        return self.nombre

