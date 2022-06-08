from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'riphah',
        'USER': 'riphah',
        'PASSWORD': 'riphah',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
