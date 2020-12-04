from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.viewsets import CovidViewSet
from server.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/covid', CovidViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]
