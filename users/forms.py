from django.contrib.auth.forms import UserCreationForm, UsernameField
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
                                      "class": "common-form-input",
                                      'placeholder': 'Create you`re username', }),
    )
    email = forms.CharField(
        label="",
        strip=False,
        widget=forms.TextInput(attrs={"autocomplete": "new-mail",
                                      "class": "common-form-input",
                                      'placeholder': 'Enter you`re mail', }),
    )
    password1 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "common-form-input",
                                          'placeholder': 'Create you`re password', }),
        help_text=None,
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "common-form-input",
                                          'placeholder': 'Wrong password again', }),
        strip=False,
        help_text=None,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class UserAddAvatar(forms.Form):
    avatar = forms.ImageField(
        required=False,
        label='',
        widget=forms.ClearableFileInput(attrs={'class': 'common-form-input'})
    )

    class Meta:
        model = User
        fields = 'avatar'


class UserChangeDetailInfo(forms.ModelForm):
    first_name = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={"class": "common-form-input",
                                      'placeholder': 'Enter you`re name'}),
    )
    last_name = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(attrs={"class": "common-form-input",
                                      'placeholder': 'Enter you`re last name'}),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name")
        field_classes = {"username": UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        first_name = self.fields.get("first_name")
        last_name = self.fields.get("last_name")
        user_permissions = self.fields.get("user_permissions")
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related(
                "content_type"
            )
