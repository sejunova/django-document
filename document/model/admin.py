from django.contrib import admin

# Register your models here.
from .models import Place, Restaurant, Waiter

admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
