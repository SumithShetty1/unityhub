"""
ASGI config for mychat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
# mychat/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from base.consumers import ChatConsumer  # Ensure this points to your ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mychat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handle HTTP requests
    "websocket": AuthMiddlewareStack(  # Handle WebSocket connections
        URLRouter(
            [
                # Define your WebSocket URL routing here
                path("ws/chat/<str:room_name>/", ChatConsumer.as_asgi()),  # WebSocket URL for chat
            ]
        )
    ),
})
