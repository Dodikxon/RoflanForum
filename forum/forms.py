from django import forms
from .models import *


class CreateThemeForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={"class": "common-form-input",
                   'placeholder': 'ENTER NAME THEME'}, )
    )
    description = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={"class": "common-form-input",
                   'placeholder': 'ENTER DESCRIPTION THEME'}, )
    )

    class Meta:
        model = CreateThemeModel
        fields = ['name', 'description']
        prepopulated_fields = {"slug": ("name",)}


class ArticleForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={"class": "common-form-input",
                   'placeholder': 'ENTER NAME ARTICLE'}, )
    )
    description = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={"class": "common-form-input",
                   'placeholder': 'ENTER DESCRIPTION ARTICLE'}, )
    )

    class Meta:
        model = Article
        fields = ['name', 'description']
        prepopulated_fields = {"slug": ("name",)}
