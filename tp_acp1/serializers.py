from rest_framework import serializers

from tp_acp1.models import MedioDePago


class MedioDePagoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedioDePago
        fields = ['id', 'nombre', 'imagen']