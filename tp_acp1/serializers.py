from rest_framework import serializers

from tp_acp1.models import MedioDePago, Plato


class MedioDePagoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedioDePago
        fields = ['id', 'nombre', 'imagen']

class PlatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'precio', 'imagen', 'descripcion']