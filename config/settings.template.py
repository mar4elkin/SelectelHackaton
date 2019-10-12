"""
Django settings for selectelhackaton project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from os.path import dirname, join, abspath
from os import environ

BASE_DIR = dirname(dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(environ.get('DEBUG', default=1))

DOCKER = bool(environ.get('DOCKER', default=0))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Auth apps:
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
{% if facebook or google or vk or github %}
{% if facebook %}
    'allauth.socialaccount.providers.facebook',  # enabled by configure {% endif %}
{% if google %}
    'allauth.socialaccount.providers.google',  # enabled by configure {% endif %}
{% if vk %}
    'allauth.socialaccount.providers.vk',  # enabled by configure {% endif %}
{% if github %}
    'allauth.socialaccount.providers.github',  # enabled by configure {% endif %}

    #'allauth.socialaccount.providers.dropbox',
    #'allauth.socialaccount.providers.linkedin',
    # etc
{% endif %}    
# lib's
    'django_extensions',
    'bootstrap4', # optional module for making bootstrap forms easier
    "taggit",
    'import_export',

    # Projects App's
    'selectelhackaton.auth',
    'selectelhackaton.demoApp',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'selectelhackaton.urls'

WSGI_APPLICATION = 'selectelhackaton.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': environ.get('SQL_DATABASE', join(BASE_DIR, 'db.sqlite3')),
        'USER': environ.get('SQL_USER', 'user'),
        'PASSWORD': environ.get('SQL_PASSWORD', 'password'),
        'HOST': environ.get('SQL_HOST', 'localhost'),
        'PORT': environ.get('SQL_PORT', '5432'),
    }
}
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# PROJECT_DIR = dirname(abspath(__file__))
STATIC_ROOT = join(BASE_DIR, 'static')
# 

STATICFILES_DIRS = (
    join(BASE_DIR, "asseets"),
)
# Authentication

AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)

TEMPLATES = [
    {
    #'TEMPLATE_DEBUG': True,
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        # allauth templates: you could copy this directory into your
        # project and tweak it according to your needs
        # join(PROJECT_ROOT, 'templates', 'uniform', 'allauth'),
        # example project specific templates
        join(BASE_DIR, 'selectelhackaton', 'templates', 'plain', 'example'),
        #join(BASE_DIR, 'selectelhackaton', 'templates', 'bootstrap', 'allauth'),
        join(BASE_DIR, 'selectelhackaton', 'templates', 'allauth'),
        join(BASE_DIR, 'selectelhackaton', 'templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            # needed for admin templates
            'django.contrib.auth.context_processors.auth',
            # these *may* not be needed
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
            # allauth needs this from django
            'django.template.context_processors.request',
            # allauth specific context processors
            #'allauth.account.context_processors.account',
            #'allauth.socialaccount.context_processors.socialaccount',
          ],
       },
    }
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1
AUTH_USER_MODEL = 'selectelhackaton_auth.User'
LOGIN_REDIRECT_URL = '/member/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
# ACCOUNT_EMAIL_VERIFICATION = 'none'  # testing...
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
SOCIALACCOUNT_AUTO_SIGNUP = False  # require social accounts to use the signup form ... I think

{% if facebook or google or vk or github %}
# For custom sign-up form:
# http://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
SOCIALACCOUNT_PROVIDERS = {
    {% if facebook %}
    'facebook': {
        'SCOPE': ['email'],  #, 'publish_stream'],
        'METHOD': 'oauth2'  # 'js_sdk'  # instead of 'oauth2'
    },{% endif %}{% if google %}
    'google':
        { 'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': { 'access_type': 'online' }
    },{% endif %}{% if vk %}
    'vk': {
        'SCOPE': ['email'],
        'METHOD': 'oauth2'
    },{% endif %}{% if github %}
    'github': {
        'SCOPE': ['email'],
        'METHOD': 'oauth2'
    },{% endif %}
}{% endif %}

