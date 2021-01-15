from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import email_address_exists
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions

UserModel = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'is_staff']


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)


    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError("A user is already registered with this e-mail address.", "already_exists")
        return email

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'password': self.validated_data.get('password', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)


    def _validate_email(self, email, password):
        if email and password:
            user = self.authenticate(username=email, password=password)
        else:
            raise exceptions.ValidationError('Must include "email" and "password".')

        return user

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            UserModel.objects.get(email__iexact=email)
        except UserModel.DoesNotExist:
            raise exceptions.ValidationError('User does not exist', 'user_does_not_exist')

        user = self._validate_email(email, password)

        if user:
            if not user.is_active:
                raise exceptions.ValidationError('User account is disabled.', 'account_not_active')
        else:
            raise exceptions.ValidationError('Wrong credentials.', 'wrong_credentials')

        email_address = user.emailaddress_set.get(email=user.email)
        if not email_address.verified:
            raise serializers.ValidationError('Account not verified.', 'account_not_verified')

        attrs['user'] = user

        return attrs

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
