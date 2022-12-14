from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('forum.urls')),
    path('', TemplateView.as_view(template_name='home.html', ), name='home'),
]
