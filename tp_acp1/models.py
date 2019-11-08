import datetime

from django.db import models


class MedioDePago(models.Model):
    nombre = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to='imagenes/', null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'

    class Meta:
        verbose_name = 'Medio de Pago'
        verbose_name_plural = 'Medios de pago'


class Filtro(models.Model):
    nombre = models.CharField(max_length=80)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'

    class Meta:
        verbose_name = 'Filtro'
        verbose_name_plural = 'Filtros'


class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


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

    class Meta:
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'


class Promocion(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=400)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + '-Habilitado' if self.activo else '-Deshabilitado'

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'


class MenuDelDia(models.Model):
    #TODO: agregar campo fecha
    entrada = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, related_name='+')
    plato_principal = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, related_name='+')
    bebida = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, related_name='+')
    postre = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, related_name='+')
    precio = models.CharField(max_length=30)
    cafe = models.BooleanField()
    activo = models.BooleanField(default=True)
    fecha = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.fecha.strftime('%d-%m-%Y') + '-Habilitado' if self.activo else '-Deshabilitado'

    class Meta:
        verbose_name = 'Menu del dia'
        verbose_name_plural = 'Menus del dia'


class Sugerencia(models.Model):
    email = models.EmailField(null=True)
    nombre = models.CharField(max_length=120)
    sugerencia = models.CharField(max_length=800)

    def __str__(self):
        return self.nombre + self.email

    class Meta:
        verbose_name = 'Sugerencia'
        verbose_name_plural = 'Sugerencias'