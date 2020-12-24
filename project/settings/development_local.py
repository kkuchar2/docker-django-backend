from util import envv

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'klkucharski-api.com',
    "192.168.0.104",
    "0.0.0.0"
]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [
    'http://localhost',
    'http://localhost:8080'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': envv('MYSQL_DATABASE'),
        'USER': envv('MYSQL_USER'),
        'PASSWORD': envv('MYSQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 3307,
    }
}