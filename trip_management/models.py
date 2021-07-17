from django.db import models
from django.db.models.fields import TextField
from django.shortcuts import reverse


# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=50)    
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name ="Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.location_name

    # def get_absolute_url(self):
    #     return reverse("trip-management:single-category", kwargs={'id': self.id})


class Route(models.Model):
    route_name = models.CharField(max_length=50)
    start_point= models.OneToOneField("Location", related_name="start_point", on_delete=models.CASCADE)
    end_point= models.OneToOneField("Location", related_name="end_point", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"

    def __str__(self):
        return self.route_name

    # def get_absolute_url(self):
    #     return reverse("Route_detail", kwargs={"pk": self.pk})
