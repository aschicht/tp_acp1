from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from tp_acp1.models import MedioDePago
from tp_acp1.serializers import MedioDePagoSerializer

class MedioDePagoViewSet(viewsets.ModelViewSet):

    queryset = MedioDePago.objects.all().filter(activo=True)
    serializer_class = MedioDePagoSerializer

