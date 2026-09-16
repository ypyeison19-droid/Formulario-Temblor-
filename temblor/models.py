from django.db import models

class Alerta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='reportes/fotos/', blank=True, null=True)
    documento = models.FileField(upload_to='reportes/documentos/', blank=True, null=True)
    audio = models.FileField(upload_to='reportes/audios/', blank=True, null=True)
    video = models.FileField(upload_to='reportes/videos/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"