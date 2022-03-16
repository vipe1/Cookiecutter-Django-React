from .base import *
from .base import env

# SECURITY
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['{{cookiecutter.domain}}'])

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    'DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True
)
SECURE_HSTS_PRELOAD = env.bool('DJANGO_SECURE_HSTS_PRELOAD', default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    'DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', default=True
)
# =============================================================


# ADMIN
ADMIN_URL = env('DJANGO_ADMIN_URL')
# ============================================================


# STATIC
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# ============================================================
