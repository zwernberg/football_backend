from channels.generic.websocket import AsyncWebsocketConsumer
import json
import pdb

from chat.models import ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

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

    async def send_message(self, text_data):
        user = text_data['payload']['user']
        message = text_data['payload']['message']
        db_message = ChatMessage(user=user, message=message)
        db_message.save()
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user
            }
        )

    async def fetch_messages(self, data):
        # pdb.set_trace()
        messages = ChatMessage.last_20_messages()
        content = {
            'type': 'messages',
            'payload': self.messages_to_json(messages)
        }
        await self.send(json.dumps(content))

    # Receive message from room group
    async def chat_message(self, event):
        user = event['user']
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'payload': {
                'user': user,
                'message': message
            }
        }))



    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result[::-1]

    def message_to_json(self, message):
        return {
            'id': str(message.id),
            'user': message.user,
            'message': message.message,
            'created': str(message.created)
        }

    # Receive message from WebSocket
    async def receive(self, text_data):
        #pdb.set_trace()
        text_data_json = json.loads(text_data)
        if (text_data_json['payload']['type'] == 'RETRIEVE_MESSAGES'):
            await self.fetch_messages(text_data_json)
        else:
            await self.send_message(text_data_json)