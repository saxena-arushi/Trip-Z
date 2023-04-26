
from django.contrib import admin
from .models import UserDetails, Preferences, PublishedTrips

# Register your models here.

admin.site.register(UserDetails)
admin.site.register(Preferences)
admin.site.register(PublishedTrips)
