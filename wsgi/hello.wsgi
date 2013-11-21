import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'askpupkin.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
path = '/home/zdvitas/web/askpupkin'
if path not in sys.path:
    sys.path.append(path)
