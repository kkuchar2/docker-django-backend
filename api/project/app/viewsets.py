from rest_framework import viewsets

from app.serializers import *


class CovidStatsViewSet(viewsets.ModelViewSet):
    queryset = CovidStats.objects.all()
    serializer_class = CovidStatsSerializer


class CovidCalcsViewSet(viewsets.ModelViewSet):
    queryset = CovidCalcs.objects.all()
    serializer_class = CovidCalcsSerializer
