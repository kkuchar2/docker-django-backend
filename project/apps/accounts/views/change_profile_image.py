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

        print(self.request)

        if self.request.user.is_authenticated:

            try:
                user = user_model.objects.get(email=self.request.user.email)
            except Exception as e:
                print("DOES NOT EXIST")
                return JsonResponse({'status': 'error', 'data': 'User does not exist'})

            if 'img' in self.request.FILES:
                user.avatar = self.request.FILES['img']
                user.save()
                s = AvatarSerializer()
                return JsonResponse({
                    'status': 'success',
                    'data': {
                        'user': {
                            'email': self.request.user.email,
                            'is_staff': self.request.user.is_staff,
                            'avatar' : s.get_avatar_url(self.request, user)
                        },
                    }
                })

            # update_user_form = UserProfileForm(data=self.request.FILES, instance=user)
            #
            # if update_user_form.is_valid():
            #     update_user_form.save()

            return JsonResponse({
                'status': 'success',
                'data': {
                    'user': {
                        'email': self.request.user.email,
                        'is_staff': self.request.user.is_staff
                    },
                }
            })
        else:
            return JsonResponse({'status': 'error', 'data': 'Not authenticated'})
