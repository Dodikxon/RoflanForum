from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class CreateThemeModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CreateThemeModel, self).save(*args, **kwargs)

    def get_absolute_url(self, slug):
        return reverse('theme-detail', {'slug': self.name})

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=10000)
    slug = models.SlugField(null=True)
    theme = models.ManyToManyField(CreateThemeModel)

    def get_absolute_url(self, slug):
        return reverse('theme-detail', {'slug': self.name})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
