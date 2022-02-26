from django.urls import path
from datawork.consumers import MyAsyncConsumer, MySyncConsumer #WSConsumer

ws_urlpatterns = [
    # path("ws/my_count/", WSConsumer.as_asgi()),
    path('ws/my_async/', MyAsyncConsumer.as_asgi()),
    path('ws/my_sync/', MySyncConsumer.as_asgi()),
]