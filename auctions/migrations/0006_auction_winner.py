# Generated by Django 3.2 on 2021-05-13 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auction_users_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='winner',
            field=models.ForeignKey(default=None, null=True, on_delete=models.SET(models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)), related_name='acquired_item', to=settings.AUTH_USER_MODEL),
        ),
    ]
