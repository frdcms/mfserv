"""
Django settings for {{cookiecutter.project_name}} project.

Generated by 'django-admin startproject' using Django {% if cookiecutter.type == "gunicorn3_sync" %}2.1.4{% elif cookiecutter.type == "gunicorn2_sync" %}1.11.18{% endif %}.

For more information on this file, see
https://docs.djangoproject.com/en/{% if cookiecutter.type == "gunicorn3_sync" %}2.1{% elif cookiecutter.type == "gunicorn2_sync" %}1.11{% endif %}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{% if cookiecutter.type == "gunicorn3_sync" %}2.1{% elif cookiecutter.type == "gunicorn2_sync" %}1.11{% endif %}/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{% if cookiecutter.type == "gunicorn3_sync" %}2.1{% elif cookiecutter.type == "gunicorn2_sync" %}1.11{% endif %}/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'DJANGO_SECRET_KEY_TO_BE_SET'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    '{{cookiecutter.app_name}}.apps.{{cookiecutter.app_name | capitalize }}Config',
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

ROOT_URLCONF = '{{cookiecutter.project_name}}.urls'

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

WSGI_APPLICATION = '{{cookiecutter.project_name}}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/{% if cookiecutter.type == "gunicorn3_sync" %}2.1{% elif cookiecutter.type == "gunicorn2_sync" %}1.11{% endif %}/ref/settings/#databases

{% if cookiecutter.db_type == 'sqlite3' %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
{% elif cookiecutter.db_type == 'postgresql' %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{cookiecutter.db_postgres_name}}',
        'HOST': '{{cookiecutter.db_postgres_host}}',
        'USER': '{{cookiecutter.db_postgres_user}}',
        'PASSWORD': '{{cookiecutter.db_postgres_password}}',
        'PORT': '{{cookiecutter.db_postgres_port}}',
    }
}
{% endif %}

# Password validation
# https://docs.djangoproject.com/en/{% if cookiecutter.type == "gunicorn3_sync" %}2.1{% elif cookiecutter.type == "gunicorn2_sync" %}1.11{% endif %}/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/{% if cookiecutter.type == "gunicorn3_sync" %}2.1{% elif cookiecutter.type == "gunicorn2_sync" %}1.11{% endif %}/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{% if cookiecutter.type == "gunicorn3_sync" %}2.1{% elif cookiecutter.type == "gunicorn2_sync" %}1.11{% endif %}/howto/static-files/

STATIC_URL = '/{{cookiecutter.name}}/{{cookiecutter.project_name}}/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")