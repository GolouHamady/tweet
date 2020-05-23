from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hashtags.views import HashTagView
from hashtags.api.views import TagTweetAPIView
from tweets.api.views import SearchTweetAPIView
from tweets.views import TweetListView
from .views import home, SearchView
from accounts.views import UserRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', TweetListView.as_view(), name='list'),
    path(r'search/', SearchView.as_view(), name='search'),
    path(r'profiles/', include('accounts.urls', namespace='profiles')),
    path(r'tags/<str:hashtag>/', HashTagView.as_view(), name='hashtag'),
    path(r'tweets/', include('tweets.urls', namespace='tweets')),
    path(r'api/tweet/', include('tweets.api.urls', namespace='tweets-api')),
    path(r'api/', include('accounts.api.urls', namespace='profiles-api')),
    path(r'api/search/', SearchTweetAPIView.as_view(), name='search-api'),
    path(r'api/tags/<str:hashtag>/', TagTweetAPIView.as_view(), name='tag-tweet-api'),
    path(r'', include('django.contrib.auth.urls')),
    path(r'register/', UserRegisterView.as_view(), name='register'),

]

if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))