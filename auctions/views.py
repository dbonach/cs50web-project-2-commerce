from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction, Bid

def index(request):

    entry = Auction.objects.order_by('id').reverse()
    return render(request, "auctions/index.html", {
        "entry": entry,
        "nome": "teste"
    })

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

def new_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        category = request.POST["category"]
        start_bid = request.POST["bid"]
        image_url = request.POST["image-url"]
        user = User.objects.first()
        new_auction = Auction(title=title, description=description, category=category, url=image_url, user=user, last_bid=start_bid)
        new_auction.save()
        bid = Bid(user=user, bid_value=start_bid, item=new_auction)
        bid.save()

        return HttpResponseRedirect(reverse("index")) 

    return render(request, "auctions/new_listing.html")

def item(request, name, id):
    item = Auction.objects.filter(id=id)
    print(name)
    if item:
        item_name = '-'.join(item[0].title.split())
        if item_name == name:
            return render(request, "auctions/item.html", {
                "item": item[0]
            })
  
    return HttpResponse("There's no such item.")
