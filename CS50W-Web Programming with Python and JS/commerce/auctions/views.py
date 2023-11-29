from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from .models import User,Listing,Category,Bid,Comment


def index(request):
    listings = Listing.objects.filter(is_active=True)
    categories = Category.objects.all()

    return render(request, "auctions/index.html", {'listings': listings, 'categories': categories})



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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    



@login_required
def create(request):
    ##Accedemos a las categorias para que aparezcan en el select
    categories = Category.objects.all()
    context = {'categories': categories}

    ##Extraemos datos del formulario de creacion
    if request.method == "POST":
        product = request.POST["product"]
        picture_url = request.POST["picture_url"]
        description = request.POST["description"]
        bids = request.POST["bids"]
        category_id = request.POST.get("category")

        ##Seleccionamos la categoria
        category_instance = Category.objects.get(id=category_id)

        ##Creamos el nuevo listing 

        new_listing = Listing(
            product=product,
            picture_url=picture_url,
            description=description,
            user=request.user,
            is_active=True,
            category=category_instance,

        )
        new_listing.save()

        ##Crear bid:

        new_bid = Bid(bid=bids,listing=new_listing, user=request.user)
        new_bid.save()
        
        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html", context)


def listing(request,id):
    listing = get_object_or_404(Listing,id=id)
    return render(request, 'auctions/view.html', {'listing': listing})

@login_required
def bid(request, id):
    bid_update = get_object_or_404(Bid, id=id)
    if not bid_update.listing.is_active:
        raise Http404("This listing is already closed.")

    new_bid = None  # Initialize new_bid outside the if statement
    
    if request.method == "POST":
        new_bid = int(request.POST.get("new_bid"))
    
        if new_bid > bid_update.bid:
            bid_update.bid = new_bid
            bid_update.user = request.user
            bid_update.save()
        
    return render(request, 'auctions/view.html', {'listing': bid_update.listing})



def category(request, category):
    categories = Category.objects.all()
    category_object = get_object_or_404(Category, category=category)
    listings = Listing.objects.filter(category=category_object,is_active=True)
    for listing in listings:
        listing.bids = Bid.objects.filter(listing=listing)
    return render(request, 'auctions/index.html', {'listings': listings,"categories":categories})

def mylistings(request):
    listings = Listing.objects.filter(user=request.user)
    for listing in listings:
        listing.bids = Bid.objects.filter(listing=listing)
    return render(request, "auctions/mylistings.html",{'listings': listings})

def close(request,id):
    close_listing = get_object_or_404(Listing, id=id)
    if request.method == "POST":
        if close_listing.user == request.user:
            close_listing.is_active = False
            close_listing.save()
            return HttpResponseRedirect('/mylistings')
    return render(request, 'auctions/close_listing.html', {'listing': close_listing})

def watchlist(request, user_id):
    user= User.objects.get(id=user_id)
    watchlist = user.watchlist.all()
    return render(request, 'auctions/watchlist.html', {'watchlist': watchlist})

def add_to_watchlist(request,id):
    listing = get_object_or_404(Listing, id=id)
    request.user.watchlist.add(listing)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def remove_from_watchlist(request,id):
    listing = get_object_or_404(Listing, id=id)
    request.user.watchlist.remove(listing)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def comment(request,id):
    if request.method == 'POST':
        user = request.user
        comment = request.POST.get('comment')
        listing_id = request.POST.get('listing')
    
    listing = get_object_or_404(Listing, id=listing_id)
    ## Creacion comentario:

    new_comment = Comment(user=user,comments=comment,listing=listing)
    new_comment.save()

    return render(request, 'auctions/view.html', {'listing': listing})
