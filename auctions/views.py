from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction, Bid

# Dummy variables
title = "Dell inspiron 14"
description = "Aparelho usado"
start_bid = 10
image_url = "https://cnet2.cbsistatic.com/img/51A28dscx0insHKgOHcMjqndvf8=/868x488/2014/05/29/2d1aae8e-a172-4fe7-8f45-08dbbfe13d5a/dell-inspiron-14-7000-series-product-photos01.jpg"
# image_url = "https://www.mtsystems.ca/wp-content/uploads/2017/11/inspiron-14-5000-series.jpg"


def index(request):
    # return render(request, "auctions/index.html", {
    #     "title": title,
    #     "description": description,
    #     "bid": start_bid,
    #     "image_url": image_url
    # })
    entry = Auction.objects.order_by('id').reverse()
    return render(request, "auctions/index.html", {
        "entry": entry
    })
    # return HttpResponse("done")


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
        start_bid = request.POST["bid"]
        image_url = request.POST["image-url"]
        print("#")
        print(image_url)
        print("#")
        user = User.objects.first()
        new_auction = Auction(title=title, description=description, url=image_url, user=user, last_bid=start_bid)
        new_auction.save()
        bid = Bid(user=user, bid_value=start_bid, item=new_auction)
        bid.save()

        return HttpResponseRedirect(reverse("index")) 

    return render(request, "auctions/new_listing.html")