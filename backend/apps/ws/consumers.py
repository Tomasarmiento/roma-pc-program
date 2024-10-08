import json
from random import randint
from time import sleep
import time
# import websockets
import asyncio
import threading
import sys, signal

from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer
from channels.db import database_sync_to_async


from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer


from apps.ws.models import ChannelInfo
from apps.ws.utils import variables as ws_vars
from apps.ws.utils.functions import send_front_message
from apps.parameters.utils import variables as param_vars
from apps.control.utils.functions import derived_sensores_states,update_msg_error
from apps.control.utils import variables as control_vars
from apps.control.utils import routines as ctrl_rtns


# class FrontConsumer(WebsocketConsumer):
#     def connect(self):
#         return super().connect()
        
#     def disconnect(self, code):
#         return super().disconnect(code)
        
    
#     def receive(self, text_data=None, bytes_data=None):
#         count = 0
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         # ctrl_rtns.RoutineHandler().start()
#         while True:
#             try:
#                 self.send(text_data = json.dumps({
#                         'mesa_armado_1' : int(param_vars.PARAMS['mesa_armado_1']),
#                         'mesa_armado_2' : int(param_vars.PARAMS['mesa_armado_2']),
#                         'okuma_1' : int(param_vars.PARAMS['okuma_1']),
#                         'okuma_2' : int(param_vars.PARAMS['okuma_2']),
#                         'okuma_3' : int(param_vars.PARAMS['okuma_3']),
#                         'okuma_4' : int(param_vars.PARAMS['okuma_4']),
#                         'mensajes_log': ws_vars.frontState.log_messages,
#                         'plc_sensors': (control_vars.PLC_DEFAULT_VARIABLES),
#                 }))
#                 time.sleep(2)
#                 count += 1
#                 # if count == 15:
#                 #     control_vars.WEBSOCKET = False
#                 print(count)
#             except:
#                 print("exeption error")



class FrontConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.set_channel_info()
        await self.accept()
        ws_vars.front_channel_name = self.channel_name
        # while ws_vars.WEBSOCKET:
        #     # funcion para pedir valores de sensores
        #     derived_sensores_states(sensores_states_plc())
        #     msg = derived_sensores_states(sensores_states_plc())
        #     update_msg_error(msg)
        #     # print(msg)
        #     # derived_sensores_states(fake_list)
        #     # ------------------------------------------------
        #     await self.send(json.dumps({
        #         'mesa_armado_1' : int(param_vars.PARAMS['mesa_armado_1']),
        #         'mesa_armado_2' : int(param_vars.PARAMS['mesa_armado_2']),
        #         'okuma_1' : int(param_vars.PARAMS['okuma_1']),
        #         'okuma_2' : int(param_vars.PARAMS['okuma_2']),
        #         'okuma_3' : int(param_vars.PARAMS['okuma_3']),
        #         'okuma_4' : int(param_vars.PARAMS['okuma_4']),
        #         'mensajes_log': ws_vars.frontState.log_messages,
        #         'plc_sensors': (control_vars.PLC_DEFAULT_VARIABLES),
        #         }))
        #     ws_vars.frontState.log_messages = []
            
        #     await asyncio.sleep(2)
        print("FRONT WS CONNECTED")



     
    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
    
    async def disconnected(self, close_code):
        print("Front ws disconnected, code", close_code)
        await self.delete_channel_info()
        await self.close()
        raise StopConsumer()
    
    async def front_message(self, event):
        await self.send(text_data=json.dumps(event['data']))
    
    @database_sync_to_async
    def set_channel_info(self):
        ChannelInfo.objects.create(
            source = 'front',
            name = self.channel_name,
            log = 0
        )
    
    @database_sync_to_async
    def delete_channel_info(self):
        channel_info = ChannelInfo.objects.get(name=self.channel_name)
        channel_info.delete()

# class PLC_Consumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.set_channel_info()
#         await self.accept()
#         ws_vars.front_channel_name = self.channel_name
#         print("plc WS CONNECTED")

#     async def receive(self, text_data=None, bytes_data=None):
#         print(text_data)
    
#     async def disconnected(self, close_code):
#         print("Front ws disconnected, code", close_code)
#         await self.delete_channel_info()
#         await self.close()
#         raise StopConsumer()
    
#     async def front_message(self, event):
#         await self.send(text_data=json.dumps(event['data']))
    
#     @database_sync_to_async
#     def set_channel_info(self):
#         ChannelInfo.objects.create(
#             source = 'plc',
#             name = self.channel_name,
#             log = 0
#         )
    
#     @database_sync_to_async
#     def delete_channel_info(self):
#         channel_info = ChannelInfo.objects.get(name=self.channel_name)
#         channel_info.delete()
# async def hello(websocket, path):
#     async for data in websocket:
#         print(f"Received: '{data}'")
#         await websocket.send(data)

# def between_callback():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     ws_server = websockets.serve(hello, 'localhost', 8000)

#     loop.run_until_complete(ws_server)
#     loop.run_forever() # this is missing
#     loop.close()

# async def send_receive_message(uri):
#     async with websockets.connect(uri) as websocket:
#         await websocket.send('This is some text.')
#         reply = await websocket.recv()
#         print(f"The reply is: '{reply}'")

# def client():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(send_receive_message('ws://localhost:8000'))
#     loop.close()

# if __name__ == "__main__":
#     print("main enter")
#     # daemon server thread:
#     server = threading.Thread(target=between_callback, daemon=True)
#     server.start()
#     client = threading.Thread(target=client)
#     client.start()
#     client.join()

