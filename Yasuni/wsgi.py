"""
WSGI config for Yasuni project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this files, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from static_ranges import Ranges
from dj_static import Cling, MediaCling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yasuni.settings')

application = get_wsgi_application()
application = Ranges(Cling(MediaCling(get_wsgi_application())))
