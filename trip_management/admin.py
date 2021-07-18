from django.contrib import admin

<<<<<<< HEAD
from trip_management.models import Location, Route


admin.site.register(Location)
admin.site.register(Route)
=======
# Register your models here.
from .models import *


admin.site.register(Location)
admin.site.register(Route)
admin.site.register(TripAssign)
>>>>>>> cb5409d56bcb8665d7ace9f55e768f73a1274496
