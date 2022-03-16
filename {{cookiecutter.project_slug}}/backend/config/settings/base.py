"""
Generated with Django 4.0
"""

from pathlib import Path
import environ

env = environ.Env()
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = ROOT_DIR / '{{cookiecutter.project_slug}}'


# GENERAL SETTINGS
DEBUG = False

LANGUAGE_CODE = 'en-us'
TIME_ZONE = '{{cookiecutter.timezone}}'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True
# =============================================================


# SECURITY
SECRET_KEY = env('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = []

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
# =============================================================


# APPS
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    # Authentication
    'djoser',
]

LOCAL_APPS = [
    '{{cookiecutter.project_slug}}.users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = 'users.User'
# =============================================================


# DATABASES
DATABASES = {
    'default': env.db('DATABASE_URL')
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# =============================================================


# MIDDLEWARE
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Keep it here, don't move it
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Whitenoise dependency
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# =============================================================


# URLS
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
# =============================================================


# ADMIN
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
ADMIN_URL = env('DJANGO_ADMIN_URL')
# =============================================================


# STATIC
STATIC_ROOT = str(ROOT_DIR / 'staticfiles')
STATIC_URL = 'api/static/'
STATICFILES_DIRS = [
    str(APPS_DIR / 'static')
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
# =============================================================


# REST FRAMEWORK SETUP
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]
# =============================================================