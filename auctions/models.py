from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    last_bid = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    users_watchlist = models.ManyToManyField(User, related_name="watchlist")
    winner = models.ForeignKey(User, on_delete=models.SET(user), default=None, null=True, related_name="acquired_item")
    comments = models.ManyToManyField('Comment', related_name="item")

    def __str__(self):
        return f"Item: {self.title}"

class Bid(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bid_value =  models.DecimalField(max_digits=8, decimal_places=2, default=0)
    item = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"Item: {self.item.title}, Value: {self.bid_value}, User: {self.user}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user.username}, Date: {self.date}"

class Category(models.Model):
    category = models.CharField(max_length=20)
    items = models.ManyToManyField(Auction, related_name="category")

    def __str__(self):
        return f"Category: {self.category}"