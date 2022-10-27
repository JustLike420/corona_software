from django.shortcuts import render
from .models import Posts


def game_view(request):
    posts = Posts.objects.filter(category='Game')
    return render(request, 'posts_view.html', context={'posts': posts})


def soft_view(request):
    posts = Posts.objects.filter(category='Soft')
    return render(request, 'posts_view.html', context={'posts': posts})


def plugin_view(request):
    posts = Posts.objects.filter(category='Plugin')
    return render(request, 'posts_view.html', context={'posts': posts})


def card_view(request, pk):
    post = Posts.objects.get(pk=pk)
    return render(request, 'post_view.html', context={'post': post})
