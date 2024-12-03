from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Redactor
from .forms import UserRegistrationForm

class UserRegisterView(CreateView):
    model = Redactor
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserProfileView(LoginRequiredMixin, UpdateView):
    model = Redactor
    fields = ['first_name', 'last_name', 'email', 'years_of_experience']
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

