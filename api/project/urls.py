from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.viewsets import *
from settings import settings
from viewsets import *

router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/covid_stats', CovidStatsViewSet)
router.register(r'api/covid_calcs', CovidCalcsViewSet)

static_urlpatterns = []

if settings.PRODUCTION_ENV == 'False':
    static_urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
] + static_urlpatterns
