from util import envv
from google.oauth2 import service_account
import os

DOMAIN_FRONTEND = 'https://admin.kkucharski.com'

"""
Host permissions
"""
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [DOMAIN_FRONTEND, 'https://api.kkucharski.com']
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [DOMAIN_FRONTEND, 'https://api.kkucharski.com']

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
Google Cloud Storage
"""
GS_CREDENTIALS_JSON = os.path.join(os.path.dirname(__file__), envv('GS_CREDENTIALS_JSON'))
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(GS_CREDENTIALS_JSON)
GS_PROJECT_ID = envv('GS_PROJECT_ID')
GS_BUCKET_NAME = envv('GS_BUCKET_NAME')


STATICFILES_STORAGE = 'custom_storages.GoogleCloudStaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.GoogleCloudMediaStorage'

STATIC_URL = 'https://storage.googleapis.com/{}/{}/'.format(GS_BUCKET_NAME, 'static')
STATIC_ROOT = 'static/'

MEDIA_URL = 'https://storage.googleapis.com/{}/{}/'.format(GS_BUCKET_NAME, 'media')
MEDIA_ROOT = 'media/'
