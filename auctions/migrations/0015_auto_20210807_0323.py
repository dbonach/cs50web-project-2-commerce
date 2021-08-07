# Generated by Django 3.2.3 on 2021-08-07 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_auction_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='winner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=models.SET(models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)), related_name='acquired_item', to=settings.AUTH_USER_MODEL),
        ),
    ]
