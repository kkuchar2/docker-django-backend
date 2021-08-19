from rest_framework import serializers

from apps.accounts.models import *


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user']
