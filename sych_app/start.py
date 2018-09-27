import sys

from django.conf import settings
from django.conf.urls import url
from django.core.management import execute_from_command_line
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    SECRET_KEY='jUstArandOmKey',
    ROOT_URLCONF=sys.modules[__name__],
    ALLOWED_HOSTS=['*'],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'postgres',
            'PORT': 5432,
        }
    },
    CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'memcached:11211'
        }
    }

)


def index(request):
    return HttpResponse('<h1>Hi there from DK!</h1>')


urlpatterns = [
    url(r'^$', index),
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
