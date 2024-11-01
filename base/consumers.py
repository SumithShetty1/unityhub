import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage  # Import your ChatMessage model

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_name = text_data_json['user_name']  # Get the user's name from the message data

        # Save the message to the database
        await self.save_message(self.room_name, user_name, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_name': user_name  # Include the user's name in the message event
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user_name = event['user_name']  # Retrieve the user's name from the event

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user_name': user_name  # Include the user's name in the response
        }))

    async def save_message(self, room_name, user_name, message):
        # Create and save a new chat message instance
        chat_message = ChatMessage(room_name=room_name, user_name=user_name, message=message)
        await database_sync_to_async(chat_message.save)()  # Save the message asynchronously
