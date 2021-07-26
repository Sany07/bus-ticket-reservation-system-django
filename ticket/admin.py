from django.contrib import admin

# Register your models here.
from ticket.models import *


@admin.register(TicketPrice)
class TicketPriceAdmin(admin.ModelAdmin):
    list_display = [
        # "trip_route",
        "fleet_type",
        "price",
        "updated_at"

    ]
    # list_filter = ["trip_route"]