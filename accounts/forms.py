from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Redactor


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Redactor
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Видаляємо підказки для полів
        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""

        # Змінюємо лейбли якщо потрібно
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm password"


class UserProfileEditForm(forms.ModelForm):
    profile_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={"class": "form-control-file", "accept": "image/*"}
        ),
        label="Фото профілю",
    )

    class Meta:
        model = Redactor
        fields = [
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
            "profile_image",
        ]
        labels = {
            "first_name": "Ім'я",
            "last_name": "Прізвище",
            "email": "Email адреса",
            "years_of_experience": "Років досвіду",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "years_of_experience": forms.NumberInput(attrs={"class": "form-control"}),
        }
