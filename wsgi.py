"""Simple WSGI application for the OpenDataCatalog Django project.
"""

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'opendatacatalog.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
