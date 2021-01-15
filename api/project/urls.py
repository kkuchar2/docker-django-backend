from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

from apps.accounts.views import CustomConfirmEmailView, CustomRegisterView, CustomLoginView
from apps.accounts.viewsets import *
from apps.covid.viewsets import *

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/covid_stats', CovidStatsViewSet)
router.register(r'api/covid_calcs', CovidCalcsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('api/rest-auth', include('rest_auth.urls')),
    path('api/rest-auth/register/', CustomRegisterView.as_view()),
    path('api/rest-auth/login/', csrf_exempt(CustomLoginView.as_view())),
    re_path(r'^verify-email/(?P<key>[-:\w]+)/$', CustomConfirmEmailView.as_view(), name='account_confirm_email')
]

urlpatterns += staticfiles_urlpatterns()
