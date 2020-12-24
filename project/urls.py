from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from viewsets import *
from app.viewsets import *

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/covid_stats', CovidStatsViewSet)
router.register(r'api/covid_calcs', CovidCalcsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]
