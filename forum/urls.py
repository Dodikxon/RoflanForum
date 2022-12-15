from django.urls import path, include

from users.urls import *
from .views import *


urlpatterns = [
    path('create/theme', CreateTheme.as_view(), name='theme'),
    path('create/article/', CreateArticle.as_view(), name='article'),
    path('theme/<slug:slug>/', ThemeDetail.as_view(), name='theme-detail'),
]
