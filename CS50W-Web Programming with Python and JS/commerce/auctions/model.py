from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Bid(models.Model):
    bid = models.FloatField()
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f'Comentario de {self.user}'

class Comment(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, blank=False)
    comments = models.CharField(max_length=1000, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f'Comentario de {self.user}'



class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    

class Listing(models.Model):
    product = models.CharField(max_length=100)
    picture_url = models.URLField(max_length=100000000,blank=True)
    description = models.CharField(max_length=1000,blank=True)
    watchlist = models.BooleanField(default=False)
    bids = models.ManyToManyField(Bid, related_name="listing_bid")
    comments = models.ManyToManyField(Comment,related_name="listing_comments")
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT, default=' ')

    def __str__(self):
        return self.product

