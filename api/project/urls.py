from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

from apps.accounts.views import CustomConfirmEmailView, CustomRegisterView, CustomLoginView, HelloView, SessionView, \
    CustomLogoutView, DeleteAccountView, CustomResetPasswordView

router = routers.DefaultRouter()

urlpatterns = [
    path('', admin.site.urls),
    path('api/register', CustomRegisterView.as_view()),
    path('api/confirm-email', csrf_exempt(CustomConfirmEmailView.as_view())),
    path('api/login', CustomLoginView.as_view()),
    path('api/logout', CustomLogoutView.as_view()),
    path('api/session', SessionView.as_view()),
    path('api/deleteAccount', DeleteAccountView.as_view()),
    path('api/resetPassword', CustomResetPasswordView.as_view()),
    path('api/hello', HelloView.as_view())
]

urlpatterns += staticfiles_urlpatterns()
