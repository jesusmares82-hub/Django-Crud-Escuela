
from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    fecha_nacimiento = models.DateField()


    def __str__(self):
        return self.nombre

