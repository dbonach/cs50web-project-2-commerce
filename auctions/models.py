from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(null=True)
    category = models.CharField(max_length=20, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")   

    def __str__(self):
        return f"{self.title}" 

class Bid(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bid_value =  models.DecimalField(max_digits=8, decimal_places=2, default=0)
    item = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids")

    def __srt__(self):
        return f"Item: {self.item}, value: {self.bid_value}, user: {self.user}"