from django.db import models
from tweetapp.models import Tweet
from twitteruserapp.models import TwitterUser

# Create your models here.
class Notification(models.Model):
    receiver = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name="receive")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="tweet_received")
    viewed_at = models.DateTimeField(default=None, blank=True, null=True)
