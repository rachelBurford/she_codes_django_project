from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.URLField()

    def __str__(self):
        return self.username

# Create your models here.
