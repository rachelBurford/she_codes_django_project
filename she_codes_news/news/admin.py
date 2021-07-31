from django.contrib import admin
from news.models import NewsStory

class NewsStoryAdmin(admin.ModelAdmin):
    fields = ['title','image','pub_date','content']
    list_display = ('title','author','pub_date')
    list_filter = ['pub_date']

admin.site.register(NewsStory,NewsStoryAdmin)