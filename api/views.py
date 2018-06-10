from django.shortcuts import render
from rest_framework import viewsets
from api.models import (Jogadores,Time,Grupos,Partidas)
from api.serializers import (JogadoresSerializers, TimesSerializers,
                            GruposSerializers,PartidasSerializers)


class JogadoresViewSet(viewsets.ModelViewSet):
    queryset = Jogadores.objects.all()
    serializer_class = JogadoresSerializers

class TimesViewSet(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimesSerializers 

class GruposViewSet(viewsets.ModelViewSet):
    queryset = Grupos.objects.all()
    serializer_class = GruposSerializers 

class PartidasViewSet(viewsets.ModelViewSet):
    queryset = Partidas.objects.all()
    serializer_class = PartidasSerializers
