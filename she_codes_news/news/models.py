from django.db import models

TITLE_CHOICE = [
    ('STAFF','STAFF'),
    ('MEMBER','MEMBER'),
    ('ANON','ANON')
]


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, choices=TITLE_CHOICE)
    pub_date = models.DateTimeField()
    content = models.TextField()
    
