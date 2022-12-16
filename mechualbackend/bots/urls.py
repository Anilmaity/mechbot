from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static
from .apis import livevideo



urlpatterns = [
    path('', views.index, name='index'),
    path('livevideo/', livevideo.Home, name='index'),
    path('chat', views.lobby, name='chat'),
    path('createbot', views.createbot , name="createbot")

              ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
