from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from tp_acp1.models import MedioDePago, Plato, Filtro, Promocion
from tp_acp1.serializers import MedioDePagoSerializer, PlatoSerializer, FiltroSerializer, PromocionSerializer


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