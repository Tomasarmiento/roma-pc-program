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


from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer


from apps.ws.models import ChannelInfo
from apps.ws.utils import variables as ws_vars
from apps.ws.utils.functions import send_front_message
from apps.parameters.utils import variables as param_vars
from apps.control.utils.functions import derived_sensores_states,update_msg_error
from apps.control.utils import variables as control_vars
from apps.control.utils import routines as ctrl_rtns
from apps.ws.utils.variables import OPC_variables



class FrontConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.set_channel_info()
        await self.accept()
        ws_vars.front_channel_name = self.channel_name
        print("FRONT WS CONNECTED")


    async def receive(self, text_data=None, bytes_data=None):
        print("receive")
        error_code = 4011
        await asyncio.sleep(0.5)
        while ws_vars.WEBSOCKET_front == True:
            # print("while front")
            # if ws_vars.WEBSOCKET_front == True:
            try:
                await self.front_message({
                    "type": "websocket.send",
                    "data": {
                        # 'mesa_armado_1' : int(param_vars.PARAMS['mesa_armado_1']),
                        # 'mesa_armado_2' : int(param_vars.PARAMS['mesa_armado_2']),
                        # 'okuma_1' : int(param_vars.PARAMS['okuma_1']),
                        # 'okuma_2' : int(param_vars.PARAMS['okuma_2']),
                        # 'okuma_3' : int(param_vars.PARAMS['okuma_3']),
                        # 'okuma_4' : int(param_vars.PARAMS['okuma_4']),
                        'mensajes_log': ws_vars.frontState.log_messages,
                        'plc_sensors': control_vars.PLC_DEFAULT_VARIABLES,
                        'plc_int_variables':  control_vars.PLC_DEFAULT_VARIABLES_INT,
                        'mensajes_error_log': ws_vars.frontState.err_messages,
                    },
                })
                await asyncio.sleep(OPC_variables.REFRESH_SENDFRONTDATA_TIME)
                await asyncio.sleep(0.05)
            except:
                await self.disconnected({'code': error_code})
                await self.close(error_code)
                raise


        print("la text data",text_data)
    
    async def disconnected(self, close_code):
        print("Front ws disconnected, code", close_code)
        await self.delete_channel_info()
        await self.close()
        raise StopConsumer()
    
    async def front_message(self, event):
        # print("el evento es", event)
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


