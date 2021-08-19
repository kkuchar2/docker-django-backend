from django.contrib.auth import get_user_model
from rest_framework import serializers


user_model = get_user_model()


class AvatarSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = user_model
        fields = ('avatar',)

    def get_avatar_url(self, request, user):
        photo_url = user.avatar.url
        return request.build_absolute_uri(photo_url)
