from django.contrib import admin
from django.urls import path
from .views import game_view, soft_view, plugin_view, card_view

urlpatterns = [
    path('', game_view, name='game-view'),
    path('soft/', soft_view, name='soft-view'),
    path('plugin/', plugin_view, name='plugin-view'),

    path('post/<int:pk>/', card_view, name='post')
]
