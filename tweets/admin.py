from django.contrib import admin
from .models import Tweet
from .forms import TweetModelForm


class TweetModelAdmin(admin.ModelAdmin):
	# form = TweetModelForm 
	model = Tweet 
	fields = ['parent', 'user', 'liked', 'content', 'reply']
	# class Meta:
	# 	model = Tweet 
	# 	fields = ['user', 'content']


admin.site.register(Tweet, TweetModelAdmin)