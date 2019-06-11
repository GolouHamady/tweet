from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

from .views import (
		RetweetView,
		TweetDetailView, 
		TweetListView,
		TweetCreateView,
		TweetUpdateView,
		TweetDeleteView,
)

app_name = "tweets"

urlpatterns = [
    path(r'', RedirectView.as_view(url="/")),
    path(r'create', TweetCreateView.as_view(), name='create'),
    path(r'<int:pk>/update', TweetUpdateView.as_view(), name='update'),
    path(r'<int:pk>/delete', TweetDeleteView.as_view(), name='delete'),
    path(r'<int:pk>/', TweetDetailView.as_view(), name='detail'),
    path(r'<int:pk>/retweet', RetweetView.as_view(), name='retweet'),
]


