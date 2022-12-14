from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin, ContextMixin

from forum.models import CreateThemeModel
from .forms import *
from .models import *


class TemplateView(ListView):
    model = CreateThemeModel
    context_object_name = 'theme'
    template_name = 'home.html'


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
