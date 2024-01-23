from pathlib import Path
from decouple import config
from datetime import timedelta

# from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG',cast=bool)

# ALLOWED_HOSTS = config('ALLOWED_HOSTS',default='*').split()
ALLOWED_HOSTS = ['127.0.0.1','2d95-213-109-66-242.ngrok-free.app']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'account',
    'twilio',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'category',
    'product',
    'rating',
    'order',
    'django_celery_results',
    'drf_api_logger',
    'cachalot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'drf_api_logger.middleware.api_logger_middleware.APILoggerMiddleware',
]

ROOT_URLCONF = 'shop_ada.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'shop_ada.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('NAME'),
        'USER':config('USER'),
        'PASSWORD':config('PASSWORD'),
        'HOST':config('HOST'),
        'POTR':5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "account.CustomUser"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=24),
    'BLACKLIST_AFTER_ROTATION': True ,

}
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'eldoszhantoroev@gmail.com'
EMAIL_HOST_PASSWORD = 'ygpy ffvw lrpz vlki'



TWILIO_SID = 'ACaee3b43b6493e8a51c22a5e415266abb'
TWILIO_AUTH_TOKEN = '006cbf41e60ecbf14732546b632e3dfe'
TWILIO_SENDER_PHONE = '+17178976093'



CSRF_TRUSTED_ORIGINS = ['https://2d95-213-109-66-242.ngrok-free.app']

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379",
#         'OPTIONS':{
#             'CLIENT_CLASS':'django_redis.client.DefaultClient',
#         }
#     }
# }

REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'


#Celery settings
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
# CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'



#Celery result
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_CACHE_BACKEND_OPTIONS = {
    'max_entries': 1000,
    'cull_frequency': 3,
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "main_format": {
            "format": "[{asctime}-{levelname}] {module}-{filename}: {message}",
            "style": "{",
        }
    },

    'handlers': {
        'console': {'class': 'logging.StreamHandler',
                    'formatter': 'main_format'},
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'main_format',
            'filename': '/home/eldos/shopbooks/log.log',
        }
    },

    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'product': {
            'handlers': ['file'],
            'level': 'WARNING'
        }
    }
}
DRF_API_LOGGER_DATABASE = True