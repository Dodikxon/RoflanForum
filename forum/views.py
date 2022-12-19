from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from forum.forms import *
from forum.models import *


class ThemeDetail(DetailView, ListView):
    model = CreateThemeModel
    template_name = 'forum/theme-detail.html'
    context_object_name = 'theme'
    object_list = Article.objects.all()

    def get_absolute_url(self, request, slug):
        slug = CreateThemeModel.objects.get(slug=slug)
        return render(request, self.template_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.all()
        return context


class ArticleView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'forum/article-detail.html'

    def get_absolute_url(self, request, slug, article_name):
        slug = CreateThemeModel.objects.get(slug=slug)
        article_name = Article.objects.get(slug=article_name)
        return render(request, self.template_name)


class CreateArticle(View):
    template_name = "forum/article.html"

    def get(self, request, slug):
        slug = CreateThemeModel.objects.get(slug=slug)
        context = {
            'form': ArticleForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            slug = CreateThemeModel.objects.get(slug=slug)
            form.save()
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            return redirect('home')
        context = {
            'form': ArticleForm(),
        }
        return render(request, self.template_name, context)


class CreateTheme(View):
    template_name = "forum/theme.html"

    def get(self, request):
        context = {
            'form': CreateThemeForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateThemeForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            form.save()
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
