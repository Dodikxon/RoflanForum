import profile

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


class UserDetail(models.Model):
    GENDER_CHOICES = [
        ('Men', 'M'),
        ('Women', 'W'),
    ]
    first_name = models.CharField(blank=True, max_length=50, default='no first name')
    last_name = models.CharField(blank=True, max_length=50, default='no last name')
    gender = models.CharField(choices=GENDER_CHOICES, default='Men',
                              blank=True, max_length=5)
    user = models.ManyToManyField(User, default=User)
    picture = models.ImageField(upload_to='upload/%Y/%M/%d/', blank=True)
