from django.contrib import admin

# Register your models here.
from trip_management.models import Location, Route


admin.site.register(Location)
admin.site.register(Route)