"""
Django settings for web_interface project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# https://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys/16630719#16630719
# Import/regenerate secret key upon downloading source. Live key should never go to repo
try:
    from .secret_key import SECRET_KEY
except ImportError:
    print("secret_key.py not found! Generating new secret key.")
    settings_dir = os.path.abspath(os.path.dirname(__file__))
    secret_key_filename = os.path.join( settings_dir, 'secret_key.py')
    from django.utils.crypto import get_random_string
    all_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    with open(secret_key_filename,'w') as sk_file:
        sk_file.write("SECRET_KEY = '"+
            get_random_string(50, all_chars)+
            "'"
        )
    get_random_string(50, all_chars)
    # import sys
    # sys.exit()
    from .secret_key import SECRET_KEY








# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = ')9yv30i%h9+3hq3f#1-3t+y*!#jz9l5w%)$d2#&8)w27ibeyz0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "134.79.165.105",
    "pswww-dev.slac.stanford.edu",    
]

if not DEBUG:
    FORCE_SCRIPT_NAME = '/ease'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'alert_config_app',
    'account_mgr_app'
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
if not DEBUG:
    MIDDLEWARE.append(
        'whitenoise.middleware.WhiteNoiseMiddleware'
    )


#WHITENOISE_STATIC_PREFIX = FORCE_SCRIPT_NAME
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

if not DEBUG:
    WHITENOISE_STATIC_PREFIX = '/static/'



ROOT_URLCONF = 'web_interface.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates/bases','./templates'],
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

WSGI_APPLICATION = 'web_interface.wsgi.application'


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

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

if not DEBUG:
    STATIC_URL = FORCE_SCRIPT_NAME + '/static/'
else:
    STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


EMAIL_HOST = 'psmail'
EMAIL_PORT = 25
if not DEBUG:
    LOGIN_REDIRECT_URL = FORCE_SCRIPT_NAME + '/alert/title'
else:
    LOGIN_REDIRECT_URL = '/alert/title'

ACCOUNT_ACTIVATION_DAYS = 7
