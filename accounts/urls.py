from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

from .views import UserDetailView, UserFollowView


app_name = "tweets"

urlpatterns = [
    path('<str:username>/', UserDetailView.as_view(), name='detail'),
    path('<str:username>/follow', UserFollowView.as_view(), name='follow'),
]


