"""
ASGI config for mychat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mychat.settings')

application = get_asgi_application()

# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from base.consumers import ChatConsumer  # replace 'base' with your app name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mychat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path("ws/chat/<str:room_name>/", ChatConsumer.as_asgi()),
            ]
        )
    ),
})
