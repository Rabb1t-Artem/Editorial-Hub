from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import Newspaper, Topic


class NewspaperForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(), widget=CheckboxSelectMultiple, label="Теми"
    )

    class Meta:
        model = Newspaper
        fields = ["title", "description", "content", "image", "topics"]
        labels = {
            "title": "Заголовок",
            "description": "Короткий опис",
            "content": "Зміст",
            "image": "Зображення",
        }


class NewsSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Пошук статей..."}
        ),
    )
    topics = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Теми",
    )
