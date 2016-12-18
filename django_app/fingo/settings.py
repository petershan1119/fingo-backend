"""
Django settings for fingo project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os, sys
import json
from corsheaders.defaults import default_headers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
conf = json.loads(open(os.path.join(ROOT_DIR, ".django-settings/deploy_setting.json")).read())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = conf["SECRET_KEY"]

# Email
email_config = conf['EMAIL']
EMAIL_HOST = email_config['EMAIL_HOST']
EMAIL_PORT = email_config['EMAIL_PORT']
EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if (len(sys.argv) > 1 and sys.argv[1] == "runserver") else False
# DEBUG = True
STATIC_S3 = True if DEBUG is False else False
# STATIC_S3 = True

AUTH_USER_MODEL = "member.fingouser"

ALLOWED_HOSTS = [
    "eb-fingo-real.ap-northeast-2.elasticbeanstalk.com",
    "fingo2-dev.ap-northeast-2.elasticbeanstalk.com"
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',

    'storages',
    'corsheaders',

    'member',
    'movie',
    'fingo_statistics',
    'user_statistics',
]


# rest_framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fingo.urls'

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

WSGI_APPLICATION = 'fingo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = conf["DATABASES"]

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


# CORS Settings
CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
    'http://fingo.herokuapp.com',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'PATCH',
    'POST',
)


# 3rd party setting

# Daum_API
DAUM_API_KEY = conf["DAUM_API_KEY"]

# AWS
aws_config = conf["AWS"]

if STATIC_S3 or not DEBUG:
    s3_config = aws_config["S3"]
    AWS_STORAGE_BUCKET_NAME = s3_config["AWS_STORAGE_BUCKET_NAME"]
    AWS_ACCESS_KEY_ID = aws_config["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = aws_config["AWS_SECRET_ACCESS_KEY"]
    AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

    STATIC_FILE_LOCATION = "static"
    STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, STATIC_FILE_LOCATION)
    STATICFILES_STORAGE = 'fingo.fingo_storage.StaticStorage'

    MEDIA_FILE_LOCATION = "media"
    MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIA_FILE_LOCATION)
    DEFAULT_FILE_STORAGE = 'fingo.fingo_storage.MediaStorage'
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'


# Facebook
FB_APP_ID = conf['FACEBOOK']['APP_ID']
FB_SECRET_CODE = conf['FACEBOOK']['SECRET_CODE']
FB_APP_ACCESS_TOKEN = FB_APP_ID+'|'+FB_SECRET_CODE
