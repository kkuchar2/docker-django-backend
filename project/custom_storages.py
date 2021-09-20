from abc import ABC
from urllib.parse import urljoin

from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting

class GoogleCloudStaticStorage(GoogleCloudStorage, ABC):
    bucket_name = setting('GS_BUCKET_NAME')
    location = 'static'

    def url(self, name):
        return urljoin(settings.STATIC_URL, name);


class GoogleCloudMediaStorage(GoogleCloudStorage, ABC):
    bucket_name = setting('GS_BUCKET_NAME')
    location = 'media'

    def url(self, name):
        return urljoin(settings.MEDIA_URL, name)
