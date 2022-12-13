from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import *
from .models import *


class ThemeView(ListView):
    model = CreateThemeModel
    context_object_name = 'theme'


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
            image = form.cleaned_data.get('image')
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProfileDetail(DetailView):
    model = User
    template_name = "registration/profile.html"
    context_object_name = "profile"


class Register(View):
    template_name = 'registration/registration.html'

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
