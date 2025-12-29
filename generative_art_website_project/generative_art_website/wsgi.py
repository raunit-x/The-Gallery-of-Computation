"""
WSGI config for generative_art_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'generative_art_website.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "generative_art_website.settings")

application = get_wsgi_application()

# Wrap with WhiteNoise to serve media files in production
application = WhiteNoise(application)
application.add_files(os.path.join(BASE_DIR, 'static/images'), prefix='images/')
