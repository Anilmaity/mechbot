
import asyncio
import json

import websockets
import datetime
import time
import random

#
#
# async def handler():
#     async with websockets.connect("ws://127.0.0.1:8000/ws/controller/") as websocket:
#         while True:
#             data = {'message': "chat", 'username': "anil pc", "time": str(datetime.datetime.utcnow().time())}
#             await websocket.send(json.dumps(data))
#             time.sleep(1)
#             try:
#                 message = await websocket.recv()
#             except websockets.ConnectionClosedOK:
#                 break
#             print(message)
#
# asyncio.run(handler())


async def control_input():
    async with websockets.connect("ws://192.168.43.156:8000/ws/controller/") as websocket:
        while True:
            data = {'message': "Get_FS_data", 'time': str(datetime.datetime.utcnow().time())}


            await websocket.send(json.dumps(data))
            try:
                message = await websocket.recv()
            except websockets.ConnectionClosedOK:
                break
            # print(message)
            # convert message to json
            message = json.loads(message)
            # calculate time difference
            time_in = datetime.datetime.strptime(message['time_in'], '%H:%M:%S.%f')
            time_out = datetime.datetime.strptime(str(datetime.datetime.utcnow().time()), '%H:%M:%S.%f')
            time_diff = time_out - time_in
            # in seconds
            time_diff = int(1000*(round(time_diff.total_seconds(),3)))
            time_in = datetime.datetime.strptime(message['time_in'], '%H:%M:%S.%f')
            time_out = datetime.datetime.strptime(message['time_out'], '%H:%M:%S.%f')
            server_time_diff = time_out - time_in
            server_time_diff = int(1000*(round(server_time_diff.total_seconds(),3)))

            print(message["data"], "T " +str(time_diff) +" ms ", "S "+str(server_time_diff)+ " ms " , time_diff-server_time_diff)

asyncio.run(control_input())

# import redis
#
# redis_client = redis.Redis(host='localhost', port=6000, db=0)
# print(redis_client)
# redis_client.set('key', 'value')
# print(redis_client.get('key'))
# redis_client.delete('key')
# print(redis_client.get('key'))
# redis_client.set('key', 'value')

