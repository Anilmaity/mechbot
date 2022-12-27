import asyncio
import datetime
import json
import random
import time

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from .models import Robot
from django.contrib.auth.models import User

from .Get_FS_Data import Get_FS_Data

import json
from channels.generic.websocket import AsyncWebsocketConsumer


class controller(WebsocketConsumer):

    def connect(self):
        print("Driver")
        self.controller = Get_FS_Data()
        print("channel layer", self.channel_layer)
        print("channel name", self.channel_name)
        self.room_group_name = 'Driver'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        # send continous data in loop
        start_time = time.time()
        message = {'message': "connected", 'time': str(datetime.datetime.utcnow().time())}
        time_elapsed = time.time() - start_time
        print("sending", time_elapsed)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'FS_data',
                'message': message
            }
        )


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
        elif text_data_json['message'] == 'Get_FS_data':
            message = text_data_json['message']
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'FS_data',
                    'message': text_data_json
                }
            )


    def FS_data(self, event):
        message = event['message']
        # R = Robot.objects.get(id=1)
        #
        # for i in range(1, 7):
        #     C = R.controls.all()[0]
        #     S = C.slider.all().get(name="CH" + str(i))
        #     S.value = self.controller.axiss[i - 1]
        #     S.save()

        # R.save()
        start_time = time.time()
        while True:
            time_elapsed = time.time() - start_time
            print("sending", time_elapsed)
            # DATA CONTAINING ALL THE VALUES OF THE SLIDERS


            self.send(text_data=json.dumps({
                'type': 'FS_DATA',
                'CH1': self.controller.axiss[0],
                'CH2': self.controller.axiss[1],
                'CH3': self.controller.axiss[2],
                'CH4': self.controller.axiss[3],
                'CH5': self.controller.axiss[4],
                'CH6': self.controller.axiss[5],
                'time_in': str(datetime.datetime.utcnow().time()),
                'time_out': message['time']
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
