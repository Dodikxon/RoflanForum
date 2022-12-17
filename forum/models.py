from django.db import models
from django.urls import reverse


class Article(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=10000)
    slug = models.SlugField(null=True)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class CreateThemeModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(null=True)
    article = models.ManyToManyField(Article)

    def get_absolute_url(self):
        return reverse("theme-detail", kwargs={"slug": self.name})

    def __str__(self):
        return self.name
