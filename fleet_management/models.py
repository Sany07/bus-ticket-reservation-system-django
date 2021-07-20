from django.db import models



class FleetType(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FleetType"
        verbose_name_plural = "FleetTypes"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("FleetType_detail", kwargs={"pk": self.pk})


class FleetName(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FleetName"
        verbose_name_plural = "FleetNames"

    def __str__(self):
        return self.name


class FleetFacility(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "FleetFacility"
        verbose_name_plural ="FleetFacilities"

    def __str__(self):
        return self.name

layout_Choices = (
        ('11', '1-1'),
        ('12', '1-2'),
        ('21', '2-1'),
        ('22', '2-2'),
    )

class FleetRegistration(models.Model):
    coach_no = models.CharField(max_length=50)
    coach_model = models.CharField(max_length=50)
    layout = models.CharField(max_length=2, choices=layout_Choices)
    fleet_type =  models.OneToOneField("FleetType", related_name="fleet_type", on_delete=models.CASCADE)
    fleet_name =  models.OneToOneField("FleetName", related_name="FleetName", on_delete=models.CASCADE)
    fleet_facility =  models.OneToOneField("FleetFacility", related_name="fleet_facility", on_delete=models.CASCADE)
    total_seat_no = models.IntegerField()
    seat_number = models.CharField(max_length=400,help_text = "Use comma to separate the input. Ex: A1 , A2 , A3 , A4 . . . ")
    is_last_seat_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "FleetRegistration"
        verbose_name_plural ="FleetRegistrations"

    def __str__(self):
        return self.coach_no