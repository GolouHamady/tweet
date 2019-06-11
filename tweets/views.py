
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views import View 
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.views.generic import (
		DetailView, 
		DeleteView,
		ListView, 
		CreateView, 
		UpdateView,
	)

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOnerMixin
from .models import Tweet 

class RetweetView(View):
	def get(self, request, pk, *args, **kwargs):
		tweet = get_object_or_404(Tweet, pk=pk)
		if request.user.is_authenticated:
			new_tweet = Tweet.objects.retweet(request.user, tweet)
			return HttpResponseRedirect('/')
		return HttpResponseRedirect(tweet.get_absolute_url())


class TweetCreateView(FormUserNeededMixin, CreateView):
	template_name = 'tweets/tweet_create.html'
	form_class = TweetModelForm 
	# success_url = reverse_lazy('tweets:create')


class TweetUpdateView(LoginRequiredMixin, UserOnerMixin, UpdateView):
	template_name = 'tweets/tweet_update.html'
	model = Tweet
	form_class = TweetModelForm 
	success_url = reverse_lazy('list')


class TweetDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'tweets/tweet_delete_confirm.html'
	model = Tweet 
	success_url = reverse_lazy('tweets:list')


class TweetDetailView(DetailView):
	template_name = 'tweets/tweet_detail.html'
	model = Tweet


class TweetListView(ListView):
	template_name = 'tweets/tweet_list.html'

	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(content__icontains=query) |
					Q(user__username__icontains=query)
				)
		return qs 

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		context['create_form'] = TweetModelForm()
		context['create_url'] = reverse_lazy("tweets:create")
		return context 
