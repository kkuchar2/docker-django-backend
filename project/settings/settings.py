from datetime import timedelta
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from util import envv
import os

PRODUCTION_ENV = envv('PRODUCTION_ENV') == 'True'

DEBUG = True

SECRET_KEY = envv('SECRET_KEY')

SETTINGS_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SETTINGS_ROOT, '../'))

DEFAULT_SITE_ID = 0

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'storages',

    # Django rest framework
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'corsheaders',

    # For social login
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    # Custom apps
    'apps.accounts',
    'apps.covid',
    'apps.crud'
]

MIDDLEWARE = [
    'apps.accounts.middleware.dynamic_site_domain_middleware.DynamicSiteDomainMiddleware',
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
    'JWT_SERIALIZER': 'dj_rest_auth.serializers.JWTSerializer',
    'JWT_TOKEN_CLAIMS_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer',
    'USER_DETAILS_SERIALIZER': 'dj_rest_auth.serializers.UserDetailsSerializer',
    'PASSWORD_RESET_SERIALIZER': 'apps.accounts.serializers.ForgotPasswordSerializer',
    'PASSWORD_RESET_CONFIRM_SERIALIZER': 'dj_rest_auth.serializers.PasswordResetConfirmSerializer',
    'PASSWORD_CHANGE_SERIALIZER': 'dj_rest_auth.serializers.PasswordChangeSerializer'
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'apps.accounts.serializers.RegisterSerializer'
}

CSRF_COOKIE_SAMESITE = 'None' if PRODUCTION_ENV else 'Lax'
SESSION_COOKIE_SAMESITE = 'None' if PRODUCTION_ENV  else 'Lax'
JWT_AUTH_SAMESITE = 'None' if PRODUCTION_ENV else 'Lax'

CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = PRODUCTION_ENV
SESSION_COOKIE_SECURE = PRODUCTION_ENV
SESSION_COOKIE_DOMAIN = ".kkucharski.com" if PRODUCTION_ENV else "0.0.0.0"
CSRF_COOKIE_DOMAIN = ".kkucharski.com" if PRODUCTION_ENV else "0.0.0.0"

# dj-rest-auth settins
REST_SESSION_LOGIN = True
REST_USE_JWT = True
JWT_AUTH_COOKIE = "auth-cookie"
JWT_AUTH_REFRESH_COOKIE = "auth-refresh-cookie"
JWT_AUTH_COOKIE_USE_CSRF = True
JWT_AUTH_SECURE = PRODUCTION_ENV

# What headers should be allowed
CORS_ALLOW_HEADERS = ['x-csrftoken', 'x-requested-with', 'content-type']

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=20),
    'ROTATE_REFRESH_TOKENS': True
}

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 1800
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_LOGOUT_ON_GET = False

"""
Sending e-mails to users
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = envv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = envv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CORS_ALLOW_CREDENTIALS = True
APPEND_SLASH = False

AVAILABLE_MODELS = [
    'apps.accounts.models.User',
    'apps.accounts.models.UserProfile',
    'apps.covid.models.CovidStats',
    'apps.covid.models.CovidCalcs',
]

"""
Sentry logging
"""
sentry_sdk.init(
    dsn=envv('SENTRY_DSN_URL'),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)


if not PRODUCTION_ENV:
    from .development import *
else:
    from .production import *
