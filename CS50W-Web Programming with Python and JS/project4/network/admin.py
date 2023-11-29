from django.contrib import admin
from .models import Tweets,User,Follow
# Register your models here.
admin.site.register(Tweets)
admin.site.register(User)
admin.site.register(Follow)