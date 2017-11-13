import os

# Base de datos - Heroku
# Update database configuration with $DATABASE_URL.
import dj_database_url

import datetime


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '54o(ku$!g0k=6ppsa-h%+znjzn1=*bmjq*bcv4&r5_&)awu_9i'

# SECURITY WARNING: don't run with debug turned on in production!
try:
    from .debug import REDZZA
    DEBUG = REDZZA
except Exception as e:
    DEBUG = True


# DEBUG = False

# Permitir todos los nombres de dominio
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'profiles.apps.ProfilesConfig',
    'categories.apps.CategoriesConfig',
    'things.apps.ThingsConfig',
    'tags.apps.TagsConfig',
    'inbox.apps.InboxConfig',
    'advertising.apps.AdvertisingConfig',
    'django_admin_env_notice',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_expiring_authtoken',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'rest_auth.registration',
    'storages',
    'rangefilter',
    'django_otp',
    'django_otp.plugins.otp_totp',
]

SITE_ID = 7

ACCOUNT_ADAPTER = 'redzza.adapter.DefaultAccountAdapterCustom'

SOCIALACCOUNT_ADAPTER = 'redzza.adapter.DefaultSocialAccountAdapterCustom'

OLD_PASSWORD_FIELD_ENABLED = True

LOGOUT_ON_PASSWORD_CHANGE = False

# EMAIL Settings
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'contacto@redzza.com'
# EMAIL_HOST_PASSWORD = 'r3dzz42017gm41l'
EMAIL_HOST_USER = 'redzzaservice@gmail.com'
EMAIL_HOST_PASSWORD = 'r3dzz42017'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_expiring_authtoken.authentication.ExpiringTokenAuthentication'
    ],
}

EXPIRING_TOKEN_LIFESPAN = datetime.timedelta(hours=24)

LOGIN_REDIRECT_URL = '/api/v1/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'redzza.urls'

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
                "django_admin_env_notice.context_processors.from_settings",
            ],
        },
    },
]

WSGI_APPLICATION = 'redzza.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if DEBUG:
    ENVIRONMENT_NAME = "Development server"
    ENVIRONMENT_COLOR = "#A0A0A0"

    OTP_TOTP_ISSUER = 'Redzza Development'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dn5515dttcdms',
            'USER': 'mhytxmydrlzlbr',
            'PASSWORD': '2d42ad1b648ec8cad34e23efe30412af165c8728c217cb247e1dc467f8a40c4b',
            'HOST': 'ec2-54-163-254-143.compute-1.amazonaws.com',
            'PORT': '5432',
        }
    }
else:
    ENVIRONMENT_NAME = "Production server"
    ENVIRONMENT_COLOR = "#FF2222"

    OTP_TOTP_ISSUER = 'Redzza Production'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'redzza',
            'USER': 'redzza',
            'PASSWORD': 'redzza852',
            'HOST': 'redzza.ctbplp1yxtbq.us-east-2.rds.amazonaws.com',
            'PORT': '5432',
        }
    }

    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': 'redzza.g5yfs8.0001.use2.cache.amazonaws.com:6379',
            'TIMEOUT': None,
            'OPTIONS': {
                'DB': 1,
                'PARSER_CLASS': 'redis.connection.HiredisParser',
            },
        }
    }

    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Base de datos - Heroku
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        },
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)i
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# Static files directories
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Docs, pictures and more
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


AWS_ACCESS_KEY_ID = 'AKIAJ22NF5J3SPKQ4F4A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'redzza'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'redzza/static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'redzza.storage_backends.MediaStorage'

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'redzza.serializers.CustomTokenSerializer',
    'PASSWORD_RESET_SERIALIZER': 'redzza.serializers.CustomPasswordResetSerializer'
}
