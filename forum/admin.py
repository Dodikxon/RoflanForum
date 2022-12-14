from django.contrib import admin
from django.contrib.admin import ModelAdmin

from forum.models import *


@admin.register(CreateThemeModel)
class ThemeAdmin(ModelAdmin):
    list_display = ("name", "slug")


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ("name", "description")
