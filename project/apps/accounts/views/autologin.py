from dj_rest_auth.app_settings import UserDetailsSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class AutoLoginView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):

        user = self.request.user

        if user.is_authenticated:
            serializer = UserDetailsSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
