from django.contrib import admin
from django.urls import path, include, URLPattern, URLResolver
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

from django.conf import settings
from django.urls import URLPattern, URLResolver

urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])


def list_urls(lis, acc=None):
    if acc is None:
        acc = []
    if not lis:
        return
    l = lis[0]
    if isinstance(l, URLPattern):
        yield acc + [str(l.pattern)]
    elif isinstance(l, URLResolver):
        yield from list_urls(l.url_patterns, acc + [str(l.pattern)])
    yield from list_urls(lis[1:], acc)


print("AVAILABLE URLS:")
for p in list_urls(urlconf.urlpatterns):
    print(''.join(p))
