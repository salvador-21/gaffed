from django.urls import path
from .consumers import WSConsumer

ws_urlpatterns =[
    path('ws/betting/',WSConsumer.as_asgi())
]