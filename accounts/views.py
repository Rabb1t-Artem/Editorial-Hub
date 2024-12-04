from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Redactor
from .forms import UserRegistrationForm, UserProfileEditForm

class UserRegisterView(CreateView):
    model = Redactor
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserProfileView(LoginRequiredMixin, DetailView):
    model = Redactor
    fields = ['first_name', 'last_name', 'email', 'years_of_experience']
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

class UserProfileEditView(LoginRequiredMixin, UpdateView):
    model = Redactor
    form_class = UserProfileEditForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')
    
    def get_object(self, queryset=None):
        return self.request.user
