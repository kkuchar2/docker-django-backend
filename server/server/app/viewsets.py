from rest_framework import viewsets
from app.models import COVID
from app.serializers import CovidSerializer


class CovidViewSet(viewsets.ModelViewSet):
    queryset = COVID.objects.all()
    serializer_class = CovidSerializer
