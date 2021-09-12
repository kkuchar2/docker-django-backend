from storages.backends.s3boto3 import S3Boto3Storage
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting
from django.conf import settings
from util import envv
from urllib.parse import urljoin

class StaticStorage(S3Boto3Storage):
    bucket_name = envv('AWS_STORAGE_BUCKET_NAME')
    location = 'static'

class MediaStorage(S3Boto3Storage):
    bucket_name = envv('AWS_STORAGE_BUCKET_NAME')
    location = 'media'

class GoogleCloudStaticStorage(GoogleCloudStorage):
    bucket_name = setting('GS_BUCKET_NAME')
    location = 'static'

    def url(self, name):
        return urljoin(settings.STATIC_URL, name);


class GoogleCloudMediaStorage(GoogleCloudStorage):
    bucket_name = setting('GS_BUCKET_NAME')
    location = 'media'

    def url(self, name):
        return urljoin(settings.MEDIA_URL, name)

