# api/urls.py
from django.urls import path
from .views import get_video_api

urlpatterns = [
    path('get-video/', get_video_api, name='get_video_api'),
]
