from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user/login')
    template_name = 'users/createAccount.html'
# Create your views here.

class AdminHomeView(generic.ListView):
    model = CustomUser
    template_name = 'users/accountInfo.html'

class UpdateDetailsView(UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    template_name = 'users/changeDetails.html'
    success_url = reverse_lazy('news:index')

    def get_object(self):
        return self.request.user