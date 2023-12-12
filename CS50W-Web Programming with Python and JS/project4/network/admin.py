from django.contrib import admin
from .models import Tweets,User,Follow,Like
# Register your models here.
admin.site.register(Tweets)
admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Like)