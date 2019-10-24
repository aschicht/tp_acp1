from django.db import models


class MedioDePago(models.Model):
    nombre = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to='imagenes/')
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre