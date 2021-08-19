from storages.backends.s3boto3 import S3Boto3Storage
from util import envv

class StaticStorage(S3Boto3Storage):
    bucket_name = envv('AWS_STORAGE_BUCKET_NAME')
    location = 'static'

class MediaStorage(S3Boto3Storage):
    bucket_name = envv('AWS_STORAGE_BUCKET_NAME')
    location = 'media'
