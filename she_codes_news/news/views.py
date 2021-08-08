from django.contrib import auth
from django.views import generic
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .forms import StoryForm
from .models import NewsStory
from django.views.generic import DetailView
from news.models import Book



class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    model = NewsStory

    # def get_queryset(self):
    #     '''Return all news stories.'''
    #     return NewsStory.objects.order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:5]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')[:6]
        return context

    # def index(request):
    #     latest_blog_list = NewsStory.objects.order_by('-pub_date')[:5]
    #     context = {'latest_blog_list': latest_blog_list}
    #     return render(request, 'news/index.html', context)


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AuthorView(ListView):
    queryset = NewsStory.objects.order_by('author')
    context_object_name = 'author_list'
    template_name = 'news/author.html'
    model = NewsStory

    def get_queryset(self):
        self.author = get_object_or_404(NewsStory, name=self.kwargs['author'])
        return NewsStory.objects.filter(author=self.author)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        # context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:5]
        # context['all_stories'] = NewsStory.objects.order_by('-pub_date')[:5]
        return context


class BookListView(ListView):
    model = Book
    template_name = 'news/booklistview.html'

    def get_queryset(self):
        self.book = get_object_or_404(Book, name=self.kwargs['author'])


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['author_stories'] = NewsStory.objects.all()
    #     # return context
