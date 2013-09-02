# This file exists only to provide an example. 
# None of the values are used in any deployed versions of the application

# Set to True in deployment mode.
DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # change name to the one created in psql
        'NAME': 'my_db',                      
        # by default the USER will be postgres
        'USER': 'example',
        # you may reset this in psql
        'PASSWORD': 'example_password',
        # leave this for development and deployment environment
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['example.com']

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'example_key'

# these settings are needed for the password recovery e-mail to appear correctly.
EMAIL_HOST = 'smtp.gmail.com'
# keep this for gmail
EMAIL_PORT = 587
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'example_password'
EMAIL_USE_TLS = True

# get from Facebook Developers
# https://developers.facebook.com/docs/opengraph/getting-started/#create-app
FACEBOOK_APP_ID = '123'

# set to your e-mail account
DEFAULT_FROM_EMAIL = 'example@gmail.com'

# set to your email
DEFAULT_FROM_EMAIL = 'example@gmail.com'

# these are quite self-explanatory after setting up the app
# in dropbox developers. See the below blog post for detailed instructions:
# http://pushingkarma.com/projects/django-dbbackup/%7B/projects/django-dbbackup/dropbox/
# also see: https://pypi.python.org/pypi/django-dbbackup

DBBACKUP_STORAGE = 'dbbackup.storage.dropbox_storage'
DBBACKUP_TOKENS_FILEPATH = '/home/example_user/Documents/dropbox_keys'
DBBACKUP_DROPBOX_APP_KEY = 'app_key'
DBBACKUP_DROPBOX_APP_SECRET = 'app_secret'
DBBACKUP_DROPBOX_ACCESS_TYPE = 'app_folder'