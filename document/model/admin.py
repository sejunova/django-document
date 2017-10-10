from django.contrib import admin

# Register your models here.
from .models import Pizza, Topping, FacebookUser, InstagramUser

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)