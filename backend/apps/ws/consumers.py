import json
from random import randint
from time import sleep

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from apps.ws.models import ChannelInfo
from apps.ws.utils import variables as ws_vars




class FrontConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.set_channel_info()
        ws_vars.front_channel_name = self.channel_name
        print("FRONT WS CONNECTED")
        await self.accept()
        # for n in range(0,100):
        #     print(n)
        #     sleep(1)
     
    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
    
    async def disconnected(self, close_code):
        print("Front ws disconnected, code", close_code)
        await self.delete_channel_info()
        await self.close()
    
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