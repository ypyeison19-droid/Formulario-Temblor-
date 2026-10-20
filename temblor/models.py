from django.db import models

class Alerta(models.Model):
    nombre_reportante = models.CharField(max_length=100)
    tipo_emergencia = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='evidencias/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_emergencia} - {self.nombre_reportante}"