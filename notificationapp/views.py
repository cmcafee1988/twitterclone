from django.shortcuts import render
from notificationapp.models import Notification
from twitteruserapp.models import TwitterUser
from django.views import View

"""class Notification(models.Model):
    receiver = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name="receive")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="tweet_received")
    status = models.BooleanField(default=False)"""



class NotificationsView(View):
    html = 'index.html'

    def get(self, request):
        new_user=TwitterUser.objects.filter(id=id)
        data = Notification.objects.filter(new_user=new_user)
        for notification in data:
            notification.delete()
        return render(request, self.html, {'data': data})
