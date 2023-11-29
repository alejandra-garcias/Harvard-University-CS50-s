from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    
    def is_following(self, other_user):
        return Follow.objects.filter(follower=self, followed=other_user).exists()

    def is_followed_by(self, other_user):
        return Follow.objects.filter(follower=other_user, followed=self).exists()


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower} follows {self.followed}'
        

class Tweets(models.Model):
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    body = models.CharField(max_length=280)  
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.body
