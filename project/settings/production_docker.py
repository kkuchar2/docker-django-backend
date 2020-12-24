from util import envv

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': envv('MYSQL_DATABASE'),
        'USER': envv('MYSQL_USER'),
        'PASSWORD': envv('MYSQL_PASSWORD'),
        'HOST': 'db',
        'PORT': 3306,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
