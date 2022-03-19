from .base import *

# GENERAL SETTINGS
DEBUG = True
# =============================================================


# SECURITY
ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
    'django'
]
# =============================================================

{%- if cookiecutter.use_mailhog == "y" %}


# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mailhog'
EMAIL_PORT = 1025
# =============================================================
{% endif %}