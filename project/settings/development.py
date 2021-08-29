import os
from util import envv

DOMAIN_FRONTEND = 'http://0.0.0.0:3000'

"""
Host permissions
"""
ALLOWED_HOSTS = ['0.0.0.0']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True

"""
Database for development is local Docker database
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'backend_db',
        'USER': 'dev',
        'PASSWORD': 'dev',
        'HOST': '127.0.0.1',
        'PORT': 3307,
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
