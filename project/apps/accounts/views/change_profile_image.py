from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from apps.accounts.serializers.avatar_serializer import AvatarSerializer

user_model = get_user_model()


class ChangeProfileImageView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    throttle_scope = 'dj_rest_auth'

    def post(self, *args, **kwargs):

        if self.request.user.is_authenticated:

            try:
                user = user_model.objects.get(email=self.request.user.email)
            except Exception as e:
                return JsonResponse({'status': 'error', 'data': 'User does not exist'})

            if 'img' in self.request.FILES:
                user.avatar.delete(save=False)
                user.avatar = self.request.FILES['img']
                user.save()
                s = AvatarSerializer()
                return JsonResponse({
                    'status': 'success',
                    'data': {
                        'avatar': s.get_avatar_url(self.request, user)
                    }

                })

            return JsonResponse({
                'status': 'error',
                'data': 'No image sent in request'
            })
        else:
            return JsonResponse({'status': 'error', 'data': 'Not authenticated'})
