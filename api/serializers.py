from rest_framework import serializers
from api.models import (Jogadores,Time,Grupos,Partidas)

class JogadoresSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Jogadores
        fields = ("__all__")

class TimesSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Time 
        fields = ("__all__")

class GruposSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Grupos
        fields = ("__all__")

class PartidasSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Partidas
        fields = ("__all__")

        