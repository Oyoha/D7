from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import PostSearch
from .forms import PostForm
from django.core.paginator import Paginator


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-public_time')
    paginate_by = 1


class NewDetailView(DetailView):
    template_name = 'new.html'
    queryset = Post.objects.all()


class NewsFilter(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostSearch(self.request.GET, queryset=self.get_queryset())
        return context


class NewsCreateView(CreateView):
    template_name = 'new_create.html'
    form_class = PostForm


class NewUpgradeView(UpdateView):
    template_name = 'new_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewDeleteView(DeleteView):
    template_name = 'new_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
