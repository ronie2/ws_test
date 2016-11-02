#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    port = 1870
    async with websockets.connect('ws://localhost:{0}'.format(port)) as websocket:

        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())
