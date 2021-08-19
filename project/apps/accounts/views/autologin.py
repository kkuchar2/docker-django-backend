from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from apps.accounts.serializers.avatar_serializer import AvatarSerializer


class AutoLoginView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    throttle_scope = 'dj_rest_auth'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            s = AvatarSerializer()

            return JsonResponse({
                'status': 'success',
                'data': {
                    'user': {
                        'email': self.request.user.email,
                        'is_staff': self.request.user.is_staff,
                        'avatar': s.get_avatar_url(self.request, self.request.user)
                    },
                }
            })
        else:
            return JsonResponse({'status': 'error', 'data': 'Not authenticated'})
