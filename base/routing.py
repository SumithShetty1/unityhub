# base/routing.py

from django.urls import path
from . import consumers  # Import your ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),  # WebSocket URL
]
