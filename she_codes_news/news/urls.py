from django.urls import path
from . import views
from news.views import AuthorView, BookListView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('books/', BookListView.as_view()),
    path('stories/<int:pk>/', AuthorView.as_view()),
]
