from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200, choices=TITLE_CHOICE)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="stories"
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField()
    
class Book(models.Model):
    title = models.ManyToManyField('NewStory'),
    author = models.ForeignKey(NewsStory,on_delete=CASCADE)