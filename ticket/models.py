from django.db import models

from fleet_management.models import FleetType
from trip_management.models import Route


class TicketPrice(models.Model):
    trip_route = models.ForeignKey(Route, related_name="ticket_trip_route", on_delete=models.CASCADE)
    fleet_type = models.ForeignKey(FleetType,related_name="ticket_fleet_type", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
        

    class Meta:
        verbose_name = "Ticket Price"
        verbose_name_plural = "Ticket Prices"

    def __str__(self):
        return f'{self.trip_route} {self.price}'

    # def get_absolute_url(self):
    #     return reverse("TicketPrice_detail", kwargs={"pk": self.pk})
