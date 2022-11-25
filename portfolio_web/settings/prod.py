from . base import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT', default=500, cast=int),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASS')
    }
}

CSRF_COOKIE_SECURE = config("CCS", default=True, cast=bool)
SESSION_COOKIE_SECURE = config("SCS", default=True, cast=bool)
CSRF_TRUSTED_ORIGINS = [config("CTO")]