from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

from tweets.api.views import (
	TweetListAPIView,
)

app_name = "tweets"

urlpatterns = [

    path(r'<str:username>/tweet/', TweetListAPIView.as_view(), name='list'),
]
