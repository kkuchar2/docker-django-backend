from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'klkucharski.com']

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [
    'http://localhost',
    'http://localhost:8080',
]
