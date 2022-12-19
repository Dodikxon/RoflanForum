from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from forum.models import CreateThemeModel, Article
from .forms import *
from .models import *


class HomePage(ListView):
    model = CreateThemeModel
    template_name = 'home.html'
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.all()[:3]
        return context



class ProfileDetail(DetailView):
    model = User
    template_name = "registration/profile.html"
    context_object_name = "profile"


class ChangeAvatar(View):
    template_name = 'registration/change_avatar.html'

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        context = {
            'form': UserAddAvatar(),
        }
        return render(request, self.template_name, context)

    def post(self, request, user_id):
        form = UserAddAvatar(request.POST)
        if form.is_valid():
            user = User.objects.get(id=user_id)
            avatar = request.FILES['avatar']
            user.avatar = avatar
            user.save()
            form = UserAddAvatar(request.POST)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ChangeProfile(View):
    template_name = 'registration/add_profile_detail.html'

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        context = {
            'form': UserChangeDetailInfo(),
        }
        return render(request, self.template_name, context)

    def post(self, request, user_id):
        form = UserChangeDetailInfo(request.POST)
        if form.is_valid():
            user = User.objects.get(id=user_id)
            first = request.POST['first_name']
            last = request.POST['last_name']
            user.first_name = first
            user.last_name = last
            user.save()
            form = UserChangeDetailInfo(request.POST, instance=user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class Register(View):
    template_name = 'registration/registration.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
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
