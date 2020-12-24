import os

# Whether it should be production environment
from util import envv

PRODUCTION_ENV = envv('PRODUCTION_ENV')

DEBUG = PRODUCTION_ENV == 'False'

# True - uses database in Docker
DOCKER_DB = envv('DOCKER_DB') == 'True'

# Get Django secret key from environment variable
SECRET_KEY = envv('SECRET_KEY')

INSTALLED_APPS = [
    'celery_kuchkr',
    'app',
    'rest_framework',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Template processors
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Rest framework permissions
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}

# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
SETTINGS_ROOT = os.path.dirname(os.path.abspath(__file__))
SERVER_APP_ROOT = os.path.join(SETTINGS_ROOT, '../server')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SERVER_APP_ROOT, '', 'static')

# Urls
ROOT_URLCONF = 'urls'

# ASGI
ASGI_APPLICATION = 'asgi.application'

# Set additional settings based on working environment
if PRODUCTION_ENV == 'False':
    if DOCKER_DB:
        print("Development Docker environment")
        from .development_docker import *
    else:
        print("Development Local environment")
        from .development_local import *
else:
    print("Production Docker environment")
    from .production_docker import *
