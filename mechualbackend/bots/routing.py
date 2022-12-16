from django.urls import re_path 
from . import controller


websocket_urlpatterns = [
    re_path('ws/controller/', controller.controller.as_asgi()),


]