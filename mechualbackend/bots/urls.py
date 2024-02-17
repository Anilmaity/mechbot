from django.urls import path
from . import views, Get_FS_Data

from django.conf import settings
from django.conf.urls.static import static
from .apis import livevideo

urlpatterns = [
                  path('', views.index, name='index'),
                  path('video_feed/', views.video_feed, name='video_feed'),
                  path('webcam_feed/', views.webcam_feed, name='webcam_feed'),

                  path('livecam_feed/', views.livecam_feed, name='livecam_feed')

              ]