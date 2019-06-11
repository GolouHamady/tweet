from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

from .views import (
		TweetCreateAPIView,
		TweetListAPIView,
		RetweetAPIView,
        LikeToggleAPIView,
        TweetDetailAPIView,
)

app_name = "tweets"

urlpatterns = [
    # path(r'', RedirectView.as_view(url="/")),
    path(r'create/', TweetCreateAPIView.as_view(), name='create'),
    path(r'', TweetListAPIView.as_view(), name='list'),
    path(r'<int:pk>/', TweetDetailAPIView.as_view(), name='detail'),
    path(r'<int:pk>/retweet/', RetweetAPIView.as_view(), name='retweet'),
    path(r'<int:pk>/like', LikeToggleAPIView.as_view(), name='like-toggle'),
    # path(r'<int:pk>/delete', TweetDeleteView.as_view(), name='delete'),
    # path(r'detail/<int:pk>/', TweetDetailView.as_view(), name='detail'),
]
