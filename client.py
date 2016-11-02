#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    port = 1870
    host = '172.17.0.2'
    async with websockets.connect('ws://{0}:{1}'.format(host, port)) as websocket:

        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())
