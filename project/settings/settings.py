import os
from datetime import timedelta

import environ

SETTINGS_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SETTINGS_ROOT, '../'))
PROJECT_PARENT_ROOT = os.path.join(PROJECT_ROOT, '../../')

env = environ.Env(DEBUG=(bool, False))

PRODUCTION_ENV = False

# Load environment variable file when running locally (i.e. Pycharm IDE)
if env('LOCAL_RUN') == 'True':
    env_file = os.path.join(PROJECT_PARENT_ROOT, '.env.dev')
    environ.Env.read_env(env_file)
else:
    PRODUCTION_ENV = env('PRODUCTION_ENV') == 'True'

DEBUG = True
SECRET_KEY = env('SECRET_KEY')
SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',

    # Django rest framework
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'corsheaders',

    # For social login
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    # Custom apps
    'apps.api',
    'apps.accounts',
    'apps.covid',
    'apps.crud',
    'apps.config'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'apps', 'accounts', 'templates')],
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

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),
)

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'apps.accounts.auth_backends.EmailBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTH_USER_MODEL = "accounts.User"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

ROOT_URLCONF = 'urls'
ASGI_APPLICATION = 'asgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Language specific settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# What is the default account adapter class
ACCOUNT_ADAPTER = 'apps.accounts.adapter.AccountAdapter'

# Which serializers are used by dj-rest-auth
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'apps.accounts.serializers.LoginSerializer',
    'TOKEN_SERIALIZER': 'dj_rest_auth.serializers.TokenSerializer',
    'USER_DETAILS_SERIALIZER': 'apps.accounts.serializers.CustomUserDetailSerializer',
    'JWT_SERIALIZER': 'dj_rest_auth.serializers.JWTSerializer',
    'JWT_TOKEN_CLAIMS_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer',
    'PASSWORD_RESET_SERIALIZER': 'apps.accounts.serializers.ForgotPasswordSerializer',
    'PASSWORD_RESET_CONFIRM_SERIALIZER': 'dj_rest_auth.serializers.PasswordResetConfirmSerializer',
    'PASSWORD_CHANGE_SERIALIZER': 'dj_rest_auth.serializers.PasswordChangeSerializer'
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'apps.accounts.serializers.RegisterSerializer'
}

CSRF_COOKIE_SAMESITE = 'None' if PRODUCTION_ENV else 'Lax'
JWT_AUTH_SAMESITE = 'None' if PRODUCTION_ENV else 'Lax'

CSRF_COOKIE_HTTPONLY = False  # Should it be true?
CSRF_COOKIE_SECURE = PRODUCTION_ENV
CSRF_COOKIE_DOMAIN = ".kkucharski.com" if PRODUCTION_ENV else "0.0.0.0"

# dj-rest-auth settings
REST_SESSION_LOGIN = False
REST_USE_JWT = True
JWT_AUTH_COOKIE = "auth-cookie"
JWT_AUTH_REFRESH_COOKIE = "auth-refresh-cookie"
JWT_AUTH_COOKIE_USE_CSRF = True
JWT_AUTH_SECURE = PRODUCTION_ENV

# What headers should be allowed
CORS_ALLOW_HEADERS = ['x-csrftoken', 'x-requested-with', 'content-type']

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 1800
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

"""
Sending e-mails to users
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CORS_ALLOW_CREDENTIALS = True
APPEND_SLASH = False

AVAILABLE_MODELS = [
    'apps.accounts.models.User',
    'apps.accounts.models.UserProfile',
    'apps.covid.models.CovidStats',
    'apps.covid.models.CovidCalcs',
]

DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024

if PRODUCTION_ENV:
    from .production import *
else:
    from .development import *
