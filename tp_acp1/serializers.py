from rest_framework import serializers

from tp_acp1.models import MedioDePago, Plato, Filtro, Promocion, MenuDelDia


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


class PromocionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promocion
        fields = ['id', 'nombre', 'descripcion']


class MenuDelDiaSerializer(serializers.HyperlinkedModelSerializer):
    entrada = PlatoSerializer(read_only=True)
    plato_principal = PlatoSerializer(read_only=True)
    postre = PlatoSerializer(read_only=True)

    class Meta:
        model = MenuDelDia
        fields = ['entrada', 'plato_principal', 'postre', 'cafe', 'precio', 'opciones']
        depth = 2


