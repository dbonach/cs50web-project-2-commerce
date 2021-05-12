# Generated by Django 3.2 on 2021-05-11 18:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auction_last_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='users_watchlist',
            field=models.ManyToManyField(related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]