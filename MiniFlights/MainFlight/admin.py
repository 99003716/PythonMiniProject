from django.contrib import admin
from .models import *

# Register your models here.
class Flightadmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class Passengeradmin(admin.ModelAdmin):
    filter_horizontal = ("flights", )
    
admin.site.register(Airport)
admin.site.register(Flight, Flightadmin)
admin.site.register(Passenger, Passengeradmin)