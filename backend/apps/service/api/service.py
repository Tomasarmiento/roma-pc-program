import asyncio
import time
import websockets

import django

from threading import Thread
import threading

from ctypes import *

# from apps.service.acdp.acdp import ACDP_UDP_PORT, ACDP_IP_ADDR
# from .protocols import UDPProtocol, ws_client, ws_data_client
from apps.ws.utils.functions import send_front_message,get_front_states
# from apps.service.api.protocols import ws_client_data

TIME_TO_SEC = 150 * 1000000
HOST = '127.0.0.1'

PORT = '8000'
WS_URI = "ws://localhost:8000/ws/micro/"
# data = get_front_states
data = {
        'mesa_armado_1' : 2,
        'mesa_armado_2' : 1,
    }


# async def service():
#     django.setup()
#     loop = asyncio.get_running_loop()
#     asyncio.set_event_loop(loop)
#     # loop.create_connection('ws://127.0.0.1:8000/ws/front/')
#     loop.run_until_complete(service2(),('ws://127.0.0.1:8000/ws/front/'))
#     try:
#         while True:
#             await asyncio.sleep(3600)
#             print("dentro de true")
#     finally:
#          print('finally')

# def service2():
#         print("dentro de while")
#         send_front_message(data)


# async def service():
#     loop = asyncio.get_running_loop()

#     transport, protocol = await loop.create_datagram_endpoint(
#         lambda: UDPProtocol(),
#         local_addr=(HOST,PORT)
#     )
#     asyncio.ensure_future(ws_client_data())

#     try:
#         while True:
#             send_front_message("es la data",data)
#             await asyncio.sleep(36)
#     finally:
#          transport.close()

def start_service():
    print('SERVICE READY')
    loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(loop,), daemon=True)
    # print("es T",t)
    t.start()
    asyncio.run_coroutine_threadsafe(service(), loop)
    print("raro",asyncio.run_coroutine_threadsafe(service(), loop))
    print("los threads activos son",threading.active_count())

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

# async def listen():
#     url = 'ws://127.0.0.1:8000/ws/front/'

#     async with websockets.connect(url) as ws:
#         msg = await ws.recv()
#         print(msg)

# asyncio.get_event_loop().run_until_complete(listen())

# time.sleep(5)
# while hola == False:
#     send_front_message(data)
