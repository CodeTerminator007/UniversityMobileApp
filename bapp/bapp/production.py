from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgres',
        'NAME': 'riphah',
        'USER': 'riphah',
        'PASSWORD': 'riphah',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
