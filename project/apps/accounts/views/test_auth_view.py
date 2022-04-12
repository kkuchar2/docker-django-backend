from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class TestAuthView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):

        user = self.request.user

        if user.is_authenticated:
            return Response('success', status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
