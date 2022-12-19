from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-panel'),
    path('', include('users.urls')),
    path('', include('forum.urls')),
    path('', HomePage.as_view(), name='home'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
