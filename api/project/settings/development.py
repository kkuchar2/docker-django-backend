import os

ALLOWED_HOSTS = ['0.0.0.0']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080", "http://127.0.0.1:8080", "http://0.0.0.0:5000"
]

URL_FRONT = 'http://localhost:8080/'

"""
Development database will be always local Docker one created by ./start_development_database.sh
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'backend_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'db',
        'PORT': 3306,
    }
}

"""
Development static files should be in local filesysten
"""
SETTINGS_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SETTINGS_ROOT, '../'))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, '', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '', 'media')

"""
Sending e-mails to users
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'klkucharskidevtest@gmail.com'
EMAIL_HOST_PASSWORD = 'dizswgdbbecutpdb'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CORS_ALLOW_CREDENTIALS = True

APPEND_SLASH=False