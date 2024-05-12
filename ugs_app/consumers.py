import json
from random import randint
from time import sleep
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import UserAccount,UserWallet,Games



class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
            print('Connected')
            await self.accept()

    async def disconnect(self, close_code):
         print(f'connection closed with code:{close_code}')

    async def receive(self,text_data):
          text_data_json=json.loads(text_data)
          games = await get_games()
          print(text_data_json)

          await self.send(text_data=json.dumps({
                'message': games,
          }))
    

@database_sync_to_async
def get_games():
 return Games.objects.all()[0].g_name