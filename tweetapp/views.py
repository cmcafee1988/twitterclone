
import re
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweetapp import forms, models
from notificationapp.models import Notification
from twitteruserapp.models import TwitterUser

# Create your views here.
def tweet_view(request, tweet_id):
    tweet = models.Tweet.objects.filter(id=tweet_id).first()
    return render(request, 'tweet.html', {'Tweet': tweet})


@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = forms.TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            at_user = re.findall(r'@([\w]+)', data.get('tweet'))
            new_tweet = models.Tweet.objects.create(
                tweet=data.get('tweet'),
                twitter_user=request.user
            )
            if at_user:
                for at in at_user:
                    new_notification = Notification.objects.create(
                        tweet=new_tweet,
                        receiver=TwitterUser.objects.get(username=at)
                    )
            return HttpResponseRedirect(reverse('home'))
    form = forms.TweetForm()
    return render(request, 'generic_form.html', {'form': form})