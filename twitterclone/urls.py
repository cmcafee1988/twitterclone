"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruserapp import views as twitter_user_views
from authenticationapp import views as authentication_views
from tweetapp import views as tweet_views
from notificationapp import views as notification_views


urlpatterns = [
    path('login/', authentication_views.login_view),
    path('logout/', authentication_views.logout_view),
    path('', twitter_user_views.index_view),
    path('profile/', twitter_user_views.profile_view),
    path('create/', twitter_user_views.create_user),
    path('following/', twitter_user_views.following_view),
    path('unfollow/', twitter_user_views.unfollow_view),
    path('tweet/', tweet_views.tweet_view),
    path('create/', tweet_views.create_tweet),
    path('notification/', notification_views.notifications),
    path('admin/', admin.site.urls),
]
