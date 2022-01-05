from django.urls import path

from .views import *

urlpatterns = [
    path('autoLogin', AutoLoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('confirm', ConfirmEmailView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('delete', DeleteAccountView.as_view()),
    path('changeProfileImage', ChangeProfileImageView.as_view()),
    path('forgotPassword', ForgotPasswordView.as_view()),
    path('resetPasswordConfirm', ResetPasswordConfirmView.as_view()),
    path('changePassword', ChangePasswordView.as_view()),
    path('changeEmail', ChangeEmailView.as_view()),
    path('googleLogin', GoogleLogin.as_view()),
]
