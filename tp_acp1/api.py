import datetime

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from tp_acp1.models import MedioDePago, Plato, Filtro, Promocion, MenuDelDia, Sugerencia, Categoria
from tp_acp1.serializers import MedioDePagoSerializer, PlatoSerializer, FiltroSerializer, PromocionSerializer, \
    MenuDelDiaSerializer, SugerenciaSerializer, CategoriaSerializer, CartaSerializer


class MedioDePagoViewSet(viewsets.ModelViewSet):

    queryset = MedioDePago.objects.all().filter(activo=True)
    serializer_class = MedioDePagoSerializer


class PlatoViewSet(viewsets.ModelViewSet):

    queryset = Plato.objects.all().filter(activo=True)
    serializer_class = PlatoSerializer


class FiltroViewSet(viewsets.ModelViewSet):

    queryset = Filtro.objects.all().filter(activo=True)
    serializer_class = FiltroSerializer


class PromocionViewSet(viewsets.ModelViewSet):

    queryset = Promocion.objects.all().filter(activo=True)
    serializer_class = PromocionSerializer


class MenuDelDiaViewSet(viewsets.ModelViewSet):

    queryset = MenuDelDia.objects.all().filter(activo=True)
    serializer_class = MenuDelDiaSerializer


class SugerenciaViewSet(viewsets.ModelViewSet):
    #TODO: Paginar
    queryset = Sugerencia.objects.all()
    serializer_class = SugerenciaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().filter(activo=True)
    serializer_class = CategoriaSerializer


def carta(request):
    categorias = Categoria.objects.filter(activo=True)
    carta = list()
    for c in categorias:
        platos = Plato.objects.filter(categoria=c, activo=True)

        if len(platos) > 0:
            categoria_dict = dict()
            categoria_dict['id']=c.id
            categoria_dict['nombre']=c.nombre
            ps = list()
            for p in platos:
                ps.append(PlatoSerializer(p).data)
            categoria_dict['platos']=ps
            carta.append(categoria_dict)

    return JsonResponse({'categorias': carta})
