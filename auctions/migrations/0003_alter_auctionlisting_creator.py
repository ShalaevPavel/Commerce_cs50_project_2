# Generated by Django 4.0.1 on 2022-11-07 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlisting_alter_user_is_active_comments_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='creator',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
