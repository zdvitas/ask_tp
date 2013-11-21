#
#import os
#import sys
#import django.core.handlers.wsgi
#
#path to directory of the .wgsi file ('[directory]/')
#wsgi_dir = os.path.abspath(os.path.dirname(__file__))
#path = '/home/zdvitas/web/askpupkin'
## path to project root directory (osqa '/')
#project_dir = path
#
#sys.path.append(project_dir)
#
#
#
#os.environ['PYTHON_EGG_CACHE'] = '/home/zdvitas/web/askpupkin/askpupkin/.python-egg'
#sys.path.append('/home/zdvitas/web/askpupkin/')
#sys.path.append(path)
##os.environ.setdefault("DJANGO_SETTINGS_MODULE", "askpupkin.settings")
#os.environ["DJANGO_SETTINGS_MODULE"] = "askpupkin.settings"
##os.environ['DJANGO_SETTINGS_MODULE'] ='askpupkin.settings'
#
#
#
#application =django.core.handlers.wsgi.WSGIHandler()



import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "askpupkin.settings")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()