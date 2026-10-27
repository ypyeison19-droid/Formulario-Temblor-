from django.db import models

class Alerta(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, default='Sismo / Temblor')
    descripcion = models.TextField()
    
    # Archivos guardados automáticamente en Cloudinary
    foto = models.ImageField(upload_to='evidencias/fotos/', null=True, blank=True)
    documento = models.FileField(upload_to='evidencias/documentos/', null=True, blank=True)
    audio = models.FileField(upload_to='evidencias/audios/', null=True, blank=True)
    video = models.FileField(upload_to='evidencias/videos/', null=True, blank=True)
    
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.nombre}"