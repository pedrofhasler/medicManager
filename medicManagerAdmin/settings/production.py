from .settings import *
import environ

env = environ.Env()

environ.Env.read_env()

DEBUG = False

SECRET_KEY = env(SECRET_KEY)

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}