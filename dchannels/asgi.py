"""
ASGI config for dchannels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""



import os
from django.core.asgi import get_asgi_application
from .routing import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dchannels.settings')
application = get_asgi_application()
