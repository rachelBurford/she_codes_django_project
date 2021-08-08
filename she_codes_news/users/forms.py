from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http.response import HttpResponse
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'image']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'image']

    def get_success_url(self):
        return HttpResponse("Success")