
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
    async with websockets.connect("ws://127.0.0.1:8000/ws/controller/") as websocket:
        while True:
            data = {'message': "control input",
                    'username': "anil pc",
                    "time": str(datetime.datetime.utcnow().time()),
                    "CH1": random.randint(1000, 2000),
                    "CH2": random.randint(1000, 2000),
                    "CH3": random.randint(1000, 2000),
                    "CH4": random.randint(1000, 2000),
                    "CH5": random.randint(1000, 2000),
                    "CH6": random.randint(1000, 2000),
                    }

            await websocket.send(json.dumps(data))
            time.sleep(1)
            try:
                message = await websocket.recv()
            except websockets.ConnectionClosedOK:
                break
            print(message)

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

