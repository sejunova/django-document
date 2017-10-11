from django.contrib import admin

# Register your models here.
from .models import Pizza, Topping, FacebookUser, InstagramUser, Idol, Group, Membership, User

admin.site.register(Idol)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(User)
