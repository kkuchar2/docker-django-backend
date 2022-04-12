from rest_framework import serializers


class ChangeProfileImageSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)

    def save(self, request):
        user = request.user
        user_profile = user.userprofile

        self.cleaned_data = self.get_cleaned_data()

        # Delete old avatar
        user_profile.avatar.delete(save=False)

        # Set new avatar
        user_profile.avatar = self.get_cleaned_data()['image']

        # Save user
        user_profile.save()

    def get_cleaned_data(self):
        return {
            'image': self.validated_data.get('image', None)
        }
