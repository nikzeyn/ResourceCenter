from django.contrib import admin
from bookingapp.models import Room, Level, Building 

# Register your models here.

admin.site.register(Room)
admin.site.register(Level)
admin.site.register(Building)