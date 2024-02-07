from django.contrib import admin

from doorbell.models import Borough, UserProfile, Post, Group
# Register your models here.

admin.site.register(Borough)
admin.site.register(UserProfile)

admin.site.register(Group)
admin.site.register(Post)

