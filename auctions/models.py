from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Category: {self.name}"

class Bid(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bid_value =  models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"Value: {self.bid_value}, User: {self.user}"

class Auction(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    last_bid = models.ForeignKey(Bid, on_delete=models.SET_NULL, related_name="item", null=True)
    users_watchlist = models.ManyToManyField(User, related_name="watchlist", blank=True)
    winner = models.ForeignKey(User, on_delete=models.SET(user), default=None, blank=True, null=True, related_name="acquired_item")
    comments = models.ManyToManyField('Comment', related_name="item", blank=True)
    category = models.ForeignKey(Category, related_name="items", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Item: {self.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user.username}, Date: {self.date}"
