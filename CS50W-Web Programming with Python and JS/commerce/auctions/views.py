from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User,Listing,Category,Bid


def index(request):
    listings = Listing.objects.filter(is_active=True)

    return render(request, "auctions/index.html",{'listings': listings})


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
    if request.method == "POST":
        new_bid = int(request.POST.get("new_bid"))
    
    bid_update = get_object_or_404(Bid, id=id)

    if new_bid > bid_update.bid:
        bid_update.bid = new_bid
        bid_update.user = request.user
        bid_update.save()
        
    return render(request, 'auctions/view.html', {'listing': bid_update.listing})