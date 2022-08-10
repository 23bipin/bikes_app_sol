from django.db import models


class Bike(models.Model):
    departure_time = models.DateField(null=False)
    return_time = models.DateField(null=False)
    station_id = models.IntegerField(null=False)
    departure_station = models.CharField(max_length=120, null=False)
    destination_id = models.IntegerField(null=False)
    destination = models.CharField(max_length=120, null=False)
    distance = models.FloatField(null=False)
    duration = models.IntegerField(null=False)

    def __str__(self):
        return str(
            self.departure_time
        )  # from ::: def__str__(self): return self.departure_time
