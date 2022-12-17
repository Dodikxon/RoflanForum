from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "avatar")
