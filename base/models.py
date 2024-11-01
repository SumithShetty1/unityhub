from django.db import models
from django.contrib.auth.models import User

# Existing RoomMember model
class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)
    room_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# New ChatMessage model
class ChatMessage(models.Model):
    room_name = models.CharField(max_length=255)  # Room name for grouping messages
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who sent the message
    message = models.TextField()  # The chat message content
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of when the message was sent

    def __str__(self):
        return f"{self.user.username}: {self.message[:20]} at {self.timestamp}"
    
