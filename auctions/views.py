from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction, Bid, Comment, Category

def index(request):
    entry = Auction.objects.filter(winner=None).order_by('id').reverse()
    return render(request, "auctions/index.html", {
        "entry": entry
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
        category = Category.objects.get(name=request.POST["category"])
        start_value = request.POST["bid"]
        image_url = request.POST["image-url"]
        user = User.objects.get(pk=request.user.id)

        bid = Bid(user=user, bid_value=start_value)
        bid.save()
        
        new_auction = Auction(title=title, description=description, url=image_url, user=user, last_bid=bid, category=category)
        new_auction.save()

        return HttpResponseRedirect(reverse("index")) 

    return render(request, "auctions/new_listing.html")

def watchlist(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    user = User.objects.get(pk=request.user.id)
    watchlist = user.watchlist.all().order_by('id').reverse()

    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist
    })

def categories(request, category=None):
    if not category:
        return render(request, "auctions/categories.html")

    else:
        items_list = Category.objects.get(name=category).items.all().filter(winner=None).order_by('pk').reverse()

        return render(request, "auctions/category_items.html", {
            "items_list": items_list,
            "category": ' & '.join(category.split('-')).capitalize()
        })

def my_listings(request):
    user = User.objects.get(pk=request.user.id)
    entry = Auction.objects.all().filter(user=user).order_by('id').reverse()
    print(entry)
    return render(request, "auctions/my_listings.html", {
        "items_list": entry
    })

# Handle individual item page
def item(request, name, item_id):

    invalid_bid = False

    def verify_url(request, name, item_id):

        item = Auction.objects.filter(id=item_id)
        if item:
            item_name = '-'.join(item[0].title.split())
            if item_name == name:
                return item[0]
        return False

    def verify_post(request, item):

        if request.POST['q'] == 'bid':
            verify_bid(request, item)

        elif request.POST['q'] == 'finished':
            item.winner = Auction.objects.get(pk=item.id).last_bid.user

            item.save()

        elif request.POST['q'] == 'remove':
            user = User.objects.get(pk=request.user.id)

            if request.POST['remove']:
                item.users_watchlist.remove(user)
            else:
                item.users_watchlist.add(user)
        
        elif request.POST['q'] == 'comment':
            user = User.objects.get(pk=request.user.id)
            new_comment = Comment(user=user, text=request.POST['comment'])
            new_comment.save()
            item.comments.add(new_comment)

    def verify_bid(request, item):
        nonlocal invalid_bid

        if int(request.POST['value']) > int(item.last_bid.bid_value):

            user = User.objects.get(pk=request.user.id)
            new_bid = Bid(user=user, bid_value=int(request.POST['value']))
            new_bid.save()

            item.last_bid = new_bid
            item.save()

            invalid_bid = False

        else:
            invalid_bid = True

    item = verify_url(request, name, item_id)

    if item:
        if request.method == 'POST':
            verify_post(request, item)

        return render(request, "auctions/item.html", {
            "item": item,
            "watchlist": item.users_watchlist.filter(pk=request.user.id),
            "invalid": invalid_bid,
            "comments": item.comments.all(),
            "category": ' & '.join(item.category.name.split('-')).capitalize()
        })
  
    return render(request, "auctions/error.html")

def setup(request):

    if not bool(Category.objects.all()):
        new_category = Category(name='others')
        new_category.save()
        new_category = Category(name='auto-parts')
        new_category.save()
        new_category = Category(name='fashion-clothing')
        new_category.save()
        new_category = Category(name='books-movies-music')
        new_category.save()
        new_category = Category(name='electronics')
        new_category.save()
        new_category = Category(name='collectibles-art')
        new_category.save()
        new_category = Category(name='home-garden')
        new_category.save()
        new_category = Category(name='sporting-goods')
        new_category.save()
        new_category = Category(name='toys-hobbies')
        new_category.save()

    return HttpResponseRedirect(reverse("index"))
    