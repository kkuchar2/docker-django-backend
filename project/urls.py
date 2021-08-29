from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

from apps.accounts.views import ConfirmEmailView, RegisterView, LoginView, AutoLoginView, \
    LogoutView, DeleteAccountView, ForgotPasswordView, GoogleLogin, ResetPasswordConfirmView, ChangeProfileImageView
from apps.crud.views import ListModelsView
from apps.crud.views.get_model import GetModelView
from apps.crud.views.update_model import UpdateModelView
from apps.crud.views.add_item import AddItemView

router = routers.DefaultRouter()

urlpatterns = [
    path('', admin.site.urls),
    path('api/register', RegisterView.as_view()),
    path('api/confirm-email', csrf_exempt(ConfirmEmailView.as_view())),
    path('api/login', LoginView.as_view()),
    path('api/logout', LogoutView.as_view()),
    path('api/autoLogin', AutoLoginView.as_view()),
    path('api/deleteAccount', DeleteAccountView.as_view()),
    path('api/forgotPassword', ForgotPasswordView.as_view()),
    path('api/changeProfileImage', ChangeProfileImageView.as_view()),
    path('api/resetPasswordConfirm', ResetPasswordConfirmView.as_view()),
    path('api/googleLogin', GoogleLogin.as_view()),
    path('api/listModels', ListModelsView.as_view()),
    path('api/getModel', GetModelView.as_view()),
    path('api/updateModel', UpdateModelView.as_view()),
    path('api/addItem', AddItemView.as_view()),
    url(r'^accounts/', include('allauth.urls'), name='socialaccount_signup')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
