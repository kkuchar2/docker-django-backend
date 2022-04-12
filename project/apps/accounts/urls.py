from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import VerifyEmailView, ResendEmailVerificationView
from dj_rest_auth.views import LogoutView
from rest_framework_simplejwt.views import TokenVerifyView

from .views import *

from django.urls import path

urlpatterns = [
    path('login', CustomLoginView.as_view()),
    path('register', CustomRegisterView.as_view()),
    path('confirm', VerifyEmailView.as_view()),
    path('autologin', AutoLoginView.as_view()),
    path('verify-email', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('resend-email', ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    path('logout', LogoutView.as_view()),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh', get_refresh_view().as_view(), name='token_refresh'),
    path('delete', DeleteAccountView.as_view()),
    path('changeProfileImage', ChangeProfileImageView.as_view()),
    path('forgotPassword', ForgotPasswordView.as_view()),
    path('resetPasswordConfirm', ResetPasswordConfirmView.as_view()),
    path('changePassword', ChangePasswordView.as_view()),
    path('changeEmail', ChangeEmailView.as_view()),
    path('googleLogin', GoogleLogin.as_view()),
    path('test_auth', TestAuthView.as_view())
]
