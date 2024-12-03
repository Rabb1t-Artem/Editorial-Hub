from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Redactor

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Redactor
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Видаляємо підказки для полів
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
        # Змінюємо лейбли якщо потрібно
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm password'
