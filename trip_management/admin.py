from django.contrib import admin

from trip_management.models import *



@admin.register(Location)
class TripAssignAdmin(admin.ModelAdmin):
    list_display = [
        "location_name",
        "is_active",

    ]
    list_filter = ["location_name","is_active",]

@admin.register(Route)
class TripAssignAdmin(admin.ModelAdmin):
    list_display = [
        "route_name",
        "is_active",

    ]
    list_filter = ["route_name","start_point","end_point"]


@admin.register(TripAssign)
class TripAssignAdmin(admin.ModelAdmin):
    list_display = [
        "route_name",
        "is_active",

    ]
    list_filter = ["route_name"]
    # date_hierarchy = "trip_date"


admin.site.register(TripDateTime)