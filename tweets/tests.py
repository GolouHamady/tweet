from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Tweet 
# Create your tests here.

User = get_user_model()


class TweetModelTestCase(TestCase):
	def setUp(self):
		Tweet.objects.create(
				user=User.objects.first(),
				content='somme test',
			)

	def test_tweet_item(self):
		obj = Tweet.objects.create(
				user=User.objects.first(),
				content='somme test',
			)

		self.assertTrue(obj.content=="somme test")



	