import environ
import os
from util import envv

env = environ.Env(DEBUG=(bool, False))

DOMAIN_FRONTEND = 'http://0.0.0.0:3000'

"""
Host permissions
"""
ALLOWED_HOSTS = ['0.0.0.0']
CSRF_TRUSTED_ORIGINS = ['http://0.0.0.0:3000']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True

"""
Database for development is local Docker database
"""


# If running locally, use Docker DB external (host) port, otherwise use internal one
port = envv('MYSQL_EXTERNAL_PORT') if envv('LOCAL_RUN') == 'True' else envv('MYSQL_EXTERNAL_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': envv('MYSQL_DATABASE'),
        'USER': envv('MYSQL_USER'),
        'PASSWORD': envv('MYSQL_PASSWORD'),
        'HOST': envv('MYSQL_HOST'),
        'PORT':  port,
    }
}

"""
Development static files are in local filesystem
"""
SETTINGS_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SETTINGS_ROOT, '../'))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, '', 'static-local')

"""
Development media files are in local filesystem
"""
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '', 'media-local')
