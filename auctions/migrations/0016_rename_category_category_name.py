# Generated by Django 3.2.3 on 2021-08-07 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20210807_0323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
