from django import forms
from tweetapp.models import Tweet
from django.forms import Textarea


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["tweet"]
        widgets = {
            'tweet': Textarea(attrs={'onkeyup':"countChar(this)"})
        }