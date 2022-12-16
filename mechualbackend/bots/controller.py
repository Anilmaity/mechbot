import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync , sync_to_async
from .models import Robot
from django.contrib.auth.models import User



import json
from channels.generic.websocket import AsyncWebsocketConsumer

class controller(WebsocketConsumer):

    def connect(self):
        print("Driver")

        print("channel layer", self.channel_layer)
        print("channel name", self.channel_name)
        self.room_group_name = 'Driver'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        if text_data_json['message'] == 'chat':
            username = text_data_json['username']
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'username': username
                }
            )
        elif text_data_json['message'] == 'control input':
            message = text_data_json['message']
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': text_data_json
                }
            )



    def chat_message(self, event):
        message = event['message']
        R = Robot.objects.get(id=1)

        for i in range(1, 7):
            C = R.controls.all()[0]
            S = C.slider.all().get(name="CH" + str(i))
            S.value = int(message["CH" + str(i)])
            S.save()
            print("CH" + str(i), message["CH" + str(i)])

        R.save()
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))

    def disconnect(self, code):
        print("disconnect")
        print(code)

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )




    # def connect(self):
    #     self.room_group_name = 'test'
    #
    #     async_to_sync(self.channel_layer.group_add)(
    #         self.room_group_name,
    #         self.channel_name
    #     )
    #
    #     self.accept()
    #

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # def chat_message(self, event):
    #     message = event['message']
    #
    #     self.send(text_data=json.dumps({
    #         'type': 'chat',
    #         'message': message
    #     }))
