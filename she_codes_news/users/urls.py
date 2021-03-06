from django.urls import path
from .views import AdminHomeView, CreateAccountView, UpdateDetailsView
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('my-account/', AdminHomeView.as_view(), name='accountInfo'),
    path('accountDetails/',UpdateDetailsView.as_view(), name='updateDetails',)
]