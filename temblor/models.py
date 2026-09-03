from django.db import models

class RegistroTemblor(models.Model):
    nombre = models.CharField(max_length=100)
    magnitud = models.FloatField()
    profundidad = models.FloatField()
    rango = models.IntegerField()
    lugar = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.lugar} - {self.magnitud}"