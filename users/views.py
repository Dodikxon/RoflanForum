from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.base import TemplateResponseMixin, ContextMixin

from forum.models import CreateThemeModel, Article
from .forms import *
from .models import *
from datetime import datetime


class TemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['theme'] = CreateThemeModel.objects.all()
        context['latest_articles'] = Article.objects.all()[:3]
        return context


class ProfileDetail(DetailView, ListView):
    model = User
    template_name = "registration/profile.html"
    context_object_name = "profile"
    object_list = UserDetail.objects.all()


class Register(View):
    template_name = 'registration/registration.html'
    object_list = UserDetail.objects.all()
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password, username=username)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
