from rest_framework import serializers

from app.models import COVID


class CovidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COVID
        fields = ['id', 'date', 'count']