#!/usr/bin/env python

import asyncio
import websockets
import random

async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))

    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))

port = random.randrange(1000, 10000)
port = 1870
start_server = websockets.serve(hello, 'localhost', port)

asyncio.get_event_loop().run_until_complete(start_server)
print('Port: ', port)
asyncio.get_event_loop().run_forever()

