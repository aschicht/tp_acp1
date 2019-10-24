from django.db import models


class MedioDePago(models.Model):
    nombre = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to='imagenes/')
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else ''


class Plato(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imagenes/plato')
    descripcion = models.CharField(max_length=400)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else ''
