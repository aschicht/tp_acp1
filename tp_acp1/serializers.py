from rest_framework import serializers

from tp_acp1.models import MedioDePago, Plato, Filtro


class MedioDePagoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MedioDePago
        fields = ['id', 'nombre', 'imagen']


class FiltroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filtro
        fields = ['id', 'nombre']


class PlatoSerializer(serializers.HyperlinkedModelSerializer):
    filtros = FiltroSerializer(many=True, read_only=True)

    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'precio', 'imagen', 'descripcion', 'filtros']
        depth = 1




