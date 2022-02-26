# from channels.generic.websocket import WebsocketConsumer

# class WSConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#         for i in range(1000):
#             self.send(json.dumps({
#                 'message': randint(1,100)
#             }))
#             sleep(1)

from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected...", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Websocket Received...", event)
        print("Websocket Received  Message -", event['text'])

    def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected...", event)
        await self.send({
            'type': "websocket.accept"
        })

    async def websocket_receive(self, event):
        print("Websocket Received...", event)
        print("Websocket Received  Message -", event['text'])

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)

