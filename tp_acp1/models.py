import datetime

from django.db import models


class MedioDePago(models.Model):
    nombre = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to='imagenes/', null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'


class Filtro(models.Model):
    nombre = models.CharField(max_length=80)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'


class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'


class Plato(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imagenes/plato', null=True)
    descripcion = models.CharField(max_length=400)
    activo = models.BooleanField(default=True)
    filtros = models.ManyToManyField(Filtro, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'


class Promocion(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=400)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'


class MenuDelDia(models.Model):
    #TODO: agregar campo fecha
    entrada = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, related_name='+')
    plato_principal = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, related_name='+')
    postre = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, related_name='+')
    precio = models.CharField(max_length=30)
    cafe = models.BooleanField()
    opciones = models.CharField(max_length=400, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.fecha.strftime('%d-%m-%Y') + '-Habilitado' if self.activo else '-Deshabilitado'


class Sugerencia(models.Model):
    email = models.EmailField(null=True)
    nombre = models.CharField(max_length=120)
    sugerencia = models.CharField(max_length=800)

    def __str__(self):
        return self.nombre + self.email