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
        context['navbar'] = 'game'
        return context


class SoftView(ListView):
    model = Posts
    queryset = Posts.objects.filter(category='Soft')
    paginate_by = 4
    template_name = 'posts_view.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'soft'
        return context


class PluginView(ListView):
    model = Posts
    queryset = Posts.objects.filter(category='Plugin')
    paginate_by = 4
    template_name = 'posts_view.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'plugin'
        return context


class PostView(DetailView):
    model = Posts
    context_object_name = 'post'
    template_name = 'post_view.html'
