# !!!! This file exists only to provide an example !!!

# Deployment mode!!!
DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'my_db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'example',
        'PASSWORD': 'example_password',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['example.com']

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'generated_by_django_£$%£$$^%&$%'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'example_password'
EMAIL_USE_TLS = True

FACEBOOK_APP_ID = '609532269066908'
FACEBOOK_APP_SECRET = '2886c39224d990896d8dac1e32220537'

DEFAULT_FROM_EMAIL = 'example@gmail.com'