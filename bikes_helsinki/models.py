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
        return str(self.departure_station)


class StationDetails(models.Model):
    fid = models.IntegerField(null=False)
    id = models.IntegerField(primary_key=True, null=False)
    nimi = models.CharField(max_length=120, null=False)
    namn = models.CharField(max_length=120, null=False)
    name = models.CharField(max_length=120, null=False)
    osoite = models.CharField(max_length=120, null=False)
    adress = models.CharField(max_length=120, null=False)
    kaupunki = models.CharField(max_length=120, null=False)
    stad = models.CharField(max_length=120, null=False)
    operaator = models.CharField(max_length=120, null=False)
    capacity = models.IntegerField(null=False)
    x = models.FloatField(max_length=10, null=False)
    y = models.FloatField(max_length=10, null=False)

    def __str__(self):
        return str(self.namn)
