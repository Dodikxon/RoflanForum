from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    email = models.EmailField(_("email address"), unique=True)
    slug = models.SlugField(null=True)

    def get_absolute_url(self):
        return reverse("profile_id", kwargs={"pk": self.id})


class CreateThemeModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name
