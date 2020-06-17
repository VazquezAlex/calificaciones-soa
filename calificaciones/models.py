from django.db import models

# Create your models here.
class ListaCalificacion(models.Model):
    alumno= models.CharField('Nombre del alumno', max_length=50)
    materia = models.CharField('Materia', max_length=50)
    calificacion1 = models.IntegerField('Calificación 1')
    calificacion2 = models.IntegerField('Calificación 2')
    calificacion3 = models.IntegerField('Calificación 3')
    promedio = models.DecimalField('Promedio', max_digits=3, decimal_places=2)