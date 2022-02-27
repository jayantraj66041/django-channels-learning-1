# from channels.generic.websocket import WebsocketConsumer

# class WSConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#         for i in range(1000):
#             self.send(json.dumps({
#                 'message': randint(1,100)
#             }))
#             sleep(1)


# Websocket data communication channel stablished
from time import sleep
import asyncio
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):        # it accessed by one user only at a time
    def websocket_connect(self, event):
        print("Websocket Connected...", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Websocket Received...", event)
        print("Websocket Received  Message -", event['text'])
        for i in range(1,101):
            self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            sleep(1)

    def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):   # It accessed by multiple users at a time
    async def websocket_connect(self, event):
        print("Websocket Connected...", event)
        await self.send({
            'type': "websocket.accept"
        })

    async def websocket_receive(self, event):
        print("Websocket Received...", event)
        print("Websocket Received  Message -", event['text'])
        for i in range(1,101):
            await self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        raise StopConsumer()

