from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    email = models.EmailField(_("email address"), unique=True)
    slug = models.SlugField(null=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    avatar = models.ImageField(upload_to='upload/users/%Y/%m/%d', blank=True, null=True)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_absolute_url(self):
        return reverse("profile_id", kwargs={"pk": self.id})

