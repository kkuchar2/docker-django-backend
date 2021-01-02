from rest_framework import serializers

from app.models import *


class CovidStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CovidStats
        fields = [
            'id',
            'date',
            'cases_daily',
            'cases_cumulative',
            'deaths_daily',
            'recoveries_daily'
        ]


class CovidCalcsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CovidCalcs
        fields = [
            'id',
            'cases_daily_increase',
            'cases_cumulative_increase',
            'deaths_daily_increase',
            'recoveries_daily_increase'
        ]
