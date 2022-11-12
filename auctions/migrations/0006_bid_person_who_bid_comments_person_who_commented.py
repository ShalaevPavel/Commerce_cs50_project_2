# Generated by Django 4.0.1 on 2022-11-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctionlisting_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='person_who_bid',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='comments',
            name='person_who_commented',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
