"""
Django settings for royalAgro project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

ENV = "DEV"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
PARENT_DIR = os.path.dirname(os.path.abspath(__file__))

if ENV == "PRD":
    DEBUG = False
    ALLOWED_HOSTS = ['*']

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'support@royalagrotrade.com'
    EMAIL_HOST_PASSWORD = 'RA|Trade@5upport'
    DEFAULT_FROM_EMAIL = 'Royal Agro <support@royalagrotrade.com>'

    ADMIN_EMAIL_USER = ['support@royalagrotrade.com']

elif ENV == "TST":
    DEBUG = True
    ALLOWED_HOSTS = ['*']

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'support@royalagrotrade.com'
    EMAIL_HOST_PASSWORD = 'RA|Trade@5upport'
    DEFAULT_FROM_EMAIL = 'Royal Agro <support@royalagrotrade.com>'

    ADMIN_EMAIL_USER = ['support@royalagrotrade.com']

else:
    DEBUG = True
    ALLOWED_HOSTS = ['*']

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'support@royalagrotrade.com'
    EMAIL_HOST_PASSWORD = 'RA|Trade@5upport'
    DEFAULT_FROM_EMAIL = 'Royal Agro <support@royalagrotrade.com>'

    ADMIN_EMAIL_USER = ['support@royalagrotrade.com']


APPNAME_LOG_FOLDER = "royalAgro"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vsopfk1$+2vd7$b39*mfeo4-3a#v2+=sm11vkxkifbi%ccv$&v'

# SECURITY WARNING: don't run with debug turned on in production!

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'royalAgro/royalAgro_app/templates/'), 
                 os.path.join(BASE_DIR, 'royalAgro/royalAgro_app/templates/email'),
                 os.path.join(BASE_DIR, 'royalAgro/royalAgro_app/templates/commodities'),
                 os.path.join(BASE_DIR, 'royalAgro/royalAgro_app/templates/common'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/site_media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'royalAgro','media')


if sys.argv[0] == "mod_wsgi" or sys.argv[0].endswith("manage.py"):
    LOGGER_FILE_NAME = "app"
else:
    LOGGER_FILE_NAME = "daemonThread"



# LOGGING
##################################################################################################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'custom': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
         },
        'appfile':{
            'level':'DEBUG',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'custom',
            'filename': '/var/log/%s/app.log' %(APPNAME_LOG_FOLDER),
            'when': 'W4',
            'interval': 1,
            'backupCount': 7
        },
        'daemonfile':{
            'level':'DEBUG',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'custom',
            'filename': '/var/log/%s/daemon.log' %(APPNAME_LOG_FOLDER),
            'when': 'W4',
            'interval': 1,
            'backupCount': 7
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'app': {
            'handlers': ['appfile'],
            'level': 'INFO',
            'propagate': False,
        },
        'daemonThread': {
            'handlers': ['daemonfile'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

LOGGING_CONFIG = 'logging.config.dictConfig'

