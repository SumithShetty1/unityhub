# base/urls.py

from django.urls import path

import mychat.base.room
from . import views
from django.contrib.auth.views import LogoutView
from .routing import websocket_urlpatterns  # Import your WebSocket URL patterns

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.lobby, name='lobby'),
    path('room/<str:room_name>/', mychat.base.room.room, name='room'),  # Updated to accept room_name
    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]

# The websocket_urlpatterns will be handled in the routing.py and asgi.py
