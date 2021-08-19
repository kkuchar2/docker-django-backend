from util import envv

DOMAIN_FRONTEND = 'https://admin.kkucharski.com'

"""
Host permissions
"""
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [DOMAIN_FRONTEND]

"""
Database for production is DigitalOcean Droplet database: db.kkucharski.com
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': envv('MYSQL_DATABASE'),
        'USER': envv('MYSQL_USER'),
        'PASSWORD': envv('MYSQL_PASSWORD'),
        'HOST': envv('MYSQL_HOST'),
        'PORT': envv('MYSQL_PORT'),
        'OPTIONS': {'ssl': True}
    }
}

"""
Production static files should be connected to DigitalOcean Spaces static files storage
"""
AWS_ACCESS_KEY_ID = envv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = envv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = envv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = envv('AWS_S3_ENDPOINT_URL')
AWS_S3_CUSTOM_DOMAIN = envv('AWS_S3_CUSTOM_DOMAIN')
AWS_LOCATION = envv('AWS_LOCATION')
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_DEFAULT_ACL = 'public-read'


STATICFILES_STORAGE = 'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, 'static')
STATIC_ROOT = 'static/'

MEDIA_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, 'media')
MEDIA_ROOT = 'media/'
