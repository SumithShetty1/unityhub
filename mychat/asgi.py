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
<<<<<<< HEAD
from base.consumers import ChatConsumer  # Ensure this points to your ChatConsumer
=======
from channels.security.websocket import AllowedHostsOriginValidator
from your_app_name import routing  # Replace with your app name
>>>>>>> 01053f3c86d170232a13f847c404d87ed771c3f0

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mychat.settings')

application = ProtocolTypeRouter({
<<<<<<< HEAD
    "http": get_asgi_application(),  # Handle HTTP requests
    "websocket": AuthMiddlewareStack(  # Handle WebSocket connections
        URLRouter(
            [
                # Define your WebSocket URL routing here
                path("ws/chat/<str:room_name>/", ChatConsumer.as_asgi()),  # WebSocket URL for chat
            ]
=======
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
>>>>>>> 01053f3c86d170232a13f847c404d87ed771c3f0
        )
    ),
})
