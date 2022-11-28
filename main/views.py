from django.db.models import F
from django.views.generic import ListView, DetailView

from .models import Posts


class GameView(ListView):
    model = Posts
    queryset = Posts.objects.filter(category='Game')
    paginate_by = 4
    template_name = 'posts_view.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Game'
        return context


class SoftView(ListView):
    model = Posts
    queryset = Posts.objects.filter(category='Soft')
    paginate_by = 4
    template_name = 'posts_view.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Soft'
        return context


class PluginView(ListView):
    model = Posts
    queryset = Posts.objects.filter(category='Plugin')
    paginate_by = 4
    template_name = 'posts_view.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Plugin'
        return context


class PostView(DetailView):
    model = Posts
    context_object_name = 'post'
    template_name = 'post_view.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context
