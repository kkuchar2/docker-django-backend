from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.accounts.serializers import ChangeProfileImageSerializer
from apps.accounts.util import parse_field_errors

user_model = get_user_model()


class ChangeProfileImageView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    throttle_scope = 'api'
    serializer_class = ChangeProfileImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return Response(parse_field_errors(e), status=status.HTTP_400_BAD_REQUEST)

        serializer.save(request)

        return Response(serializer.data, status=status.HTTP_200_OK)
