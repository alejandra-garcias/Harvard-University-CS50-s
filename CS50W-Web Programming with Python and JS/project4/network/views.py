from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json

from .models import User,Tweets,Follow,Like

def unlike(request,tweet_id):
    tweet = Tweets.objects.get(pk=tweet_id)
    unlike = Like.objects.filter(user=request.user,tweet=tweet)
    unlike.delete()
    return JsonResponse({"message":"Unliked!"})

def edit(request,tweet_id):
    if request.method == "POST":
        data =  json.loads(request.body)
        edit_tweet = Tweets.objects.get(pk=tweet_id)
        edit_tweet.body = data["content"]
        edit_tweet.save()
        return JsonResponse({"message": "Edited", "data":data["content"]})


def like(request,tweet_id):
    tweet = Tweets.objects.get(pk=tweet_id)
    new_like = Like(user=request.user,tweet=tweet)
    new_like.save()
    return JsonResponse({"message":"Liked!"})

def index(request):
    tweets = Tweets.objects.all().order_by('-created_at')
    all_likes = Like.objects.all()
    you_liked = []
    try:
        for like in all_likes:
            if like.user.id == request.user.id:
                you_liked.append(like.tweet.id)
    except:
        you_liked = []

    return render(request, "network/index.html",{'tweets':tweets,'you_liked':you_liked })

   




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def tweet(request):

    #Collecting from form
    if request.method == "POST":
        user = request.user
        body = request.POST["body"]
    
    #Creating tweet:

    new_tweet = Tweets(user=user,body=body)
    new_tweet.save()
    return HttpResponseRedirect(reverse("index"))


def profile(request,id):
    profile = get_object_or_404(User, id=id)
    tweets = Tweets.objects.filter(user=profile).order_by('-created_at')
    following = Follow.objects.filter(follower=profile)
    followers = Follow.objects.filter(followed=profile)

    #Check if request.user follows the current profile:

    try:
        checkFollow = followers.filter(follower=User.objects.get(pk=request.user.id))
        if len(checkFollow)!=0:
            isFollowing = True
        else:
            isFollowing = False
    except:
        isFollowing = False

    return render(request, "network/profile.html",{
        'profile':profile,
        'tweets':tweets,
        'following':following,
        'followers':followers,
        'isFollowing':isFollowing
        })


@login_required
def following(request):
    # Get the users that the current user is following
    following_users = Follow.objects.filter(follower=request.user).values_list('followed', flat=True)

    # Get the tweets from the following users
    tweets = Tweets.objects.filter(user__in=following_users).order_by('-created_at')

    return render(request, 'network/index.html', {'tweets': tweets})


def follow(request):
    userfollow = request.POST['userfollow']
    userfollow = User.objects.get(username=userfollow)
    to_follow = Follow(follower=request.user, followed=userfollow)
    to_follow.save()
    # Redirige de nuevo a la página desde la que vino
    return redirect(request.META.get('HTTP_REFERER', '/'))

def unfollow(request):
    userfollow = request.POST['userfollow']
    userfollow = User.objects.get(username=userfollow)
    to_follow = Follow.objects.get(follower=request.user, followed=userfollow )
    to_follow.delete()
    # Redirige de nuevo a la página desde la que vino
    return redirect(request.META.get('HTTP_REFERER', '/'))

