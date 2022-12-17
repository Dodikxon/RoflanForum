from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', Register.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_id'),
    path('', include('forum.urls'), name='theme'),
    path('profile/change/<int:user_id>/', ChangeProfile.as_view(), name='change_profile'),
    path('profile/avatar/change/<int:user_id>/', ChangeAvatar.as_view(), name='change_avatar')
]
