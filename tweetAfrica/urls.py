from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hashtags.views import HashTagView
from tweets.views import TweetListView
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', TweetListView.as_view(), name='list'),
    path(r'profiles/', include('accounts.urls', namespace='profiles')),
    path(r'tags/<str:hashtag>/', HashTagView.as_view(), name='hashtag'),
    path(r'tweets/', include('tweets.urls', namespace='tweets')),
    path(r'api/tweet/', include('tweets.api.urls', namespace='tweets-api')),
    path(r'api/', include('accounts.api.urls', namespace='profiles-api')),

]


if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))