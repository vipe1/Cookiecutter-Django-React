from .base import *
from .base import env
{% if cookiecutter.email_provider != "none" %}
# ADDITIONAL APPS
INSTALLED_APPS += [
    'anymail', # Email integrating app
]
# =============================================================

{% endif %}
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

{%- if cookiecutter.email_provider != "none" %}


# EMAIL
EMAIL_BACKEND = 'anymail.backends.{{cookiecutter.email_provider}}.EmailBackend'
{% if cookiecutter.email_provider == "mailgun" %}
# https://anymail.readthedocs.io/en/stable/esps/mailgun/
ANYMAIL = {
    'MAILGUN_API_KEY': env('MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': env('MAILGUN_DOMAIN'),
    'MAILGUN_API_URL': env('MAILGUN_API_URL', default='https://api.mailgun.net/v3'),
}
{% elif cookiecutter.email_provider == "mailjet" %}
# https://anymail.readthedocs.io/en/stable/esps/mailjet/
ANYMAIL = {
    'MAILJET_API_KEY': env('MAILJET_API_KEY'),
    'MAILJET_SECRET_KEY': env('MAILJET_SECRET_KEY'),
}
{% elif cookiecutter.email_provider == "mandrill" %}
# https://anymail.readthedocs.io/en/stable/esps/mandrill/
ANYMAIL = {
    'MANDRILL_API_KEY': env('MANDRILL_API_KEY'),
    'MANDRILL_API_URL': env(
        'MANDRILL_API_URL', default='https://mandrillapp.com/api/1.0'
    ),
}
{% elif cookiecutter.email_provider == "postal" %}
# https://anymail.readthedocs.io/en/stable/esps/postal/
ANYMAIL = {
    'POSTAL_API_KEY': env('POSTAL_API_KEY'),
    'POSTAL_API_URL': env('POSTAL_API_URL'),
}
{% elif cookiecutter.email_provider == "postmark" %}
# https://anymail.readthedocs.io/en/stable/esps/postmark/
ANYMAIL = {
    'POSTMARK_SERVER_TOKEN': env('POSTMARK_SERVER_TOKEN'),
    'POSTMARK_API_URL': env('POSTMARK_API_URL', default='https://api.postmarkapp.com/'),
}
{% elif cookiecutter.email_provider == "sendgrid" %}
# https://anymail.readthedocs.io/en/stable/esps/sendgrid/
ANYMAIL = {
    'SENDGRID_API_KEY': env('SENDGRID_API_KEY'),
    'SENDGRID_GENERATE_MESSAGE_ID': env('SENDGRID_GENERATE_MESSAGE_ID'),
    'SENDGRID_MERGE_FIELD_FORMAT': env('SENDGRID_MERGE_FIELD_FORMAT'),
    'SENDGRID_API_URL': env('SENDGRID_API_URL', default='https://api.sendgrid.com/v3/'),
}
{% elif cookiecutter.email_provider == "sendinblue" %}
# https://anymail.readthedocs.io/en/stable/esps/sendinblue/
ANYMAIL = {
    'SENDINBLUE_API_KEY': env('SENDINBLUE_API_KEY'),
    'SENDINBLUE_API_URL': env(
        'SENDINBLUE_API_URL', default='https://api.sendinblue.com/v3/'
    ),
}
{% elif cookiecutter.email_provider == "sparkpost" %}
# https://anymail.readthedocs.io/en/stable/esps/sparkpost/
ANYMAIL = {
    'SPARKPOST_API_KEY': env('SPARKPOST_API_KEY'),
    'SPARKPOST_API_URL': env(
        'SPARKPOST_API_URL', default='https://api.sparkpost.com/api/v1'
    ),
}
{%- endif %}
# =============================================================
{% endif %}