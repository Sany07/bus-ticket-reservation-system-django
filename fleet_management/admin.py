from django.contrib import admin

from fleet_management.models import *



@admin.register(FleetType)
class TripAssignAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "is_active",

    ]
    list_filter = ["name","is_active",]



@admin.register(FleetName)
class TripAssignAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "company_name",
        "is_active",

    ]
    list_filter = ["company_name","is_active",]

admin.site.register(FleetFacility)
#class TripAssignAdmin(admin.ModelAdmin):
    # list_display = [
    #     "location_name",
    #     "is_active",

    # ]
    # list_filter = ["location_name","is_active",]

@admin.register(FleetRegistration)
class TripAssignAdmin(admin.ModelAdmin):
    list_display = [
        "coach_no",
        "fleet_name",
        "is_active",

    ]
    # list_filter = ["location_name","is_active",]