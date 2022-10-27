from django.contrib import admin
from django.urls import path
from .views import GameView, SoftView, PluginView, PostView

urlpatterns = [
    path('', GameView.as_view(), name='game-view'),
    path('soft/', SoftView.as_view(), name='soft-view'),
    path('plugin/', PluginView.as_view(), name='plugin-view'),

    path('post/<int:pk>/', PostView.as_view(), name='post')
]
