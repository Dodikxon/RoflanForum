from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import *

User = get_user_model()


class UserCreationForm(UserCreationForm):
    error_messages = {
        "password_mismatch": _(""),
    }
    username = forms.CharField(
        label="",
        strip=False,
        widget=forms.TextInput(attrs={"autocomplete": "new-username",
                                      "class": "form-login-input",
                                      'placeholder': 'Create you`re username', }),
    )
    email = forms.CharField(
        label="",
        strip=False,
        widget=forms.TextInput(attrs={"autocomplete": "new-mail",
                                      "class": "form-login-input",
                                      'placeholder': 'Enter you`re mail', }),
    )
    password1 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "form-login-input",
                                          'placeholder': 'Create you`re password', }),
        help_text=None,
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "form-login-input",
                                          'placeholder': 'Wrong password again', }),
        strip=False,
        help_text=None,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")



