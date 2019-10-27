from django.db import models


class MedioDePago(models.Model):
    nombre = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to='imagenes/')
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'


class Filtro(models.Model):
    nombre = models.CharField(max_length=80)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'


class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'


class Plato(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imagenes/plato')
    descripcion = models.CharField(max_length=400)
    activo = models.BooleanField()
    filtros = models.ManyToManyField(Filtro)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'


class Promocion(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=400)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'


class MenuDelDia(models.Model):
    #TODO: agregar campo fecha
    entrada = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, related_name='+')
    plato_principal = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, related_name='+' )
    postre = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, related_name='+')
    precio = models.CharField(max_length=30)
    cafe = models.BooleanField()
    opciones = models.CharField(max_length=400)
    activo = models.BooleanField()

    def __str__(self):
        return  '-Habilitado' if self.activo else '-Deshabilitado'


class Sugerencia(models.Model):
    email = models.EmailField(null=True)
    nombre = models.CharField(max_length=120)
    sugerencia = models.CharField(max_length=800)

    def __str__(self):
        return self.nombre