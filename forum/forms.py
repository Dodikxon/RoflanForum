from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import *


class CreateThemeForm(ModelForm):
    name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-login-input",
                   'placeholder': 'Enter name a theme'}, )
    )
    description = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-login-input",
                   'placeholder': 'Enter description a theme'}, )
    )
    slug = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-login-input",
                   'placeholder': 'Enter link on a theme', }, )
    )

    class Meta:
        model = CreateThemeModel
        fields = ['name', 'description', 'slug']


class ArticleForm(ModelForm):
    name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-login-input",
                   'placeholder': 'Enter name a article'}, )
    )
    description = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={"class": "form-login-input",
                   'placeholder': 'Enter description a article'}, )
    )

    class Meta:
        model = Article
        fields = ['name', 'description']
