from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from tp_acp1.models import MedioDePago, Plato
from tp_acp1.serializers import MedioDePagoSerializer, PlatoSerializer


class MedioDePagoViewSet(viewsets.ModelViewSet):

    queryset = MedioDePago.objects.all().filter(activo=True)
    serializer_class = MedioDePagoSerializer


class PlatoViewSet(viewsets.ModelViewSet):

    queryset = Plato.objects.all().filter(activo=True)
    serializer_class = PlatoSerializer
