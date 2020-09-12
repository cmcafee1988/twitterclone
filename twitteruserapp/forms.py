from django import forms
from twitteruserapp.models import TwitterUser


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)