
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("tweet", views.tweet,name="tweet"),
    path("profile/<int:id>", views.profile,name="profile"),
    path('follow/',views.follow,name="follow"),
    path('unfollow/',views.unfollow,name="unfollow"),
    path('following/',views.following,name="following"),
    path("edit/<int:tweet_id>", views.edit,name="edit"),
    path("unlike/<int:tweet_id>", views.unlike,name="unlike"),
    path("like/<int:tweet_id>", views.like,name="like"),

    

]
