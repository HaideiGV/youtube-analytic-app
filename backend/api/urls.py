from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('channels', views.get_channel_info, name='channel_info'),
]
