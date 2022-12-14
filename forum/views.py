from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from forum.forms import *
from forum.models import *


class ThemeDetail(DetailView):
    model = CreateThemeModel
    context_object_name = 'theme'
    template_name = 'forum/theme-detail.html'



class ArticleView(View):
    model = Article
    context_object_name = 'article'
    template_name = 'forum/theme-detail.html'


class CreateArticle(View):
    template_name = "forum/article.html"

    def get(self, request):
        context = {
            'form': ArticleForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            return redirect('home')
        context = {
            'form': form
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
            form.save()
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            slug = form.cleaned_data.get('slug')
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
