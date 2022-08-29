import asyncio
import json
from collections import deque

# from django.http import response
import websockets

# from apps.service.acdp.handlers import send_command, process_rx_message, build_header
# from apps.service.acdp.handlers import IPAddress, ACDPMessage, MicroWSHandler
# from apps.service.acdp.commands import WS_CODES, COMMANDS, ROUTINE_COMMANDS
# from apps.service.acdp.messages import ACDPDataEnums
# from apps.service.acdp.messages_base import DrviverFlags
# from apps.service.acdp.acdp import ACDP_UDP_PORT
# from apps.service.acdp.handlers import AcdpMessage

TIME_TO_SEC = 150 * 1000000
HOST = '127.0.0.1'
ACDP_IP = '192.168.0.101'
PORT = '8000'
URI = "ws://localhost:8000/ws/micro/"
HOR_GRAPH_STEP = 0.1
REFRESH_TIME = 0.1          # Time to refresh states on frontend in seconds


class Buffer():
    buffer = deque()
    add_to_buffer = False
    send_data = False
    reset_data = False

class UDPProtocol(asyncio.DatagramProtocol):
    transport = ''

    def __init__(self):
        super().__init__()

    def connection_made(self, transport):       # Used by asyncio
        self.transport = transport
        UDPProtocol.transport = transport
 
    def datagram_received(self, data, addr):    # addr is tuple (IP, PORT), example ('192.168.0.28', 54208)
        print("data recibidaaaaaa",data,addr)
        print('hola')

    def error_received(self, exc: Exception) -> None:
        return super().error_received(exc)

    def connection_lost(self, exc):     # exc: (self, exc: Optional[Exception]) -> None
        # ACDPMessage.connected = False
        return super().connection_lost(exc)

async def ws_data_client():
    uri = "ws://localhost:8000/ws/graphs/"
    while True:
        await asyncio.sleep(10)


async def ws_client():
    uri = "ws://localhost:8000/ws/micro/"
    while True:
        await asyncio.sleep(10)


async def ws_client_data():
    uri = "ws://localhost:8000/ws/front/"
    while True:
        await asyncio.sleep(10)



async def ws_handler(ws):
    consumer_task = asyncio.ensure_future(ws_consumer(ws))
    producer_task_1 = asyncio.ensure_future(ws_states_update(ws))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task_1],
        return_when = asyncio.FIRST_COMPLETED
        )
    for task in pending:
        task.cancel()

async def ws_states_update(websocket):
    while True:
        await asyncio.sleep(10)

async def ws_consumer(websocket):
    while True:
        await asyncio.sleep(10)

def get_states_msg():
    return False

async def close_con(transport):     # close (udp) connection
    await asyncio.sleep(1)
    print('CLOSE CONNECTION')
    transport.close()