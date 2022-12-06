from django.contrib import admin
from django.urls import path
from .views import GameView, SoftView, PluginView, PostView, download_add

urlpatterns = [
    path('', GameView.as_view(), name='game-view'),
    path('soft/', SoftView.as_view(), name='soft-view'),
    path('plugin/', PluginView.as_view(), name='plugin-view'),

    path('post/<int:pk>/', PostView.as_view(), name='post'),
    path('post/<int:pk>/download_add', download_add, name='post_download')
]
