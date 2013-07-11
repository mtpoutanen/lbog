import os
import sys
sys.path.append('/var/www/lbog/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'lbog.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
