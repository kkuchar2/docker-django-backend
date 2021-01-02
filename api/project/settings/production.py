from api.project.util import envv

"""
Host permissions
"""


ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ['https://klkucharski.com']

"""
Database for production is DigitalOcean managed database
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': envv('MYSQL_DATABASE'),
        'USER': envv('MYSQL_USER'),
        'PASSWORD': envv('MYSQL_PASSWORD'),
        'HOST': envv('MYSQL_HOST'),
        'PORT': envv('MYSQL_PORT'),
    }
}

"""
Production static files should be connected to external static files storage
(S3 / DigitalOcean Spaces / Other)
"""
AWS_ACCESS_KEY_ID = envv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = envv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = envv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = envv('AWS_S3_ENDPOINT_URL')
AWS_LOCATION = envv('AWS_LOCATION')
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_S3_SIGNATURE_VERSION = 's3v4'

STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

"""
Caching
"""
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
