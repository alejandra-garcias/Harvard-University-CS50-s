# Generated by Django 4.1.3 on 2023-11-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_category_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='picture_url',
            field=models.URLField(max_length=100000000),
        ),
    ]