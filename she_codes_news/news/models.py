from django.db import models
from django.contrib.auth import get_user_model

TITLE_CHOICE = [
    ('STAFF','STAFF'),
    ('MEMBER','MEMBER'),
    ('ANON','ANON')
]

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200, choices=TITLE_CHOICE)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    
