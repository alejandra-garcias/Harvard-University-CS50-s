# Generated by Django 4.1.3 on 2023-11-17 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_comment_rename_bids_bid_delete_comments_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='categories',
            new_name='category',
        ),
    ]