from django.core.management.base import BaseCommand
import datetime as dt
import pandas as pd
from bikes_helsinki.models import Bike

categories = [
    "Departure_Time",
    "Return_Time",
    "StationID",
    "Departure_Station",
    "Destination_StationID",
    "Destination",
    "Distance",
    "Duration",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        df = pd.read_csv("static/data/2021-05.csv", nrows=1000)
        df.columns = categories
        # filter for duration
        df = df[~(df["Duration"] < 10)]
        df["Duration"] = df["Duration"].div(60)
        df = df.round(decimals=2)

        # filter for distance
        df = df[~(df["Distance"] < 10)]
        df["Distance"] = df["Distance"].div(1000)
        df = df.round(decimals=2)

        # date only, for test!!!
        df["Departure_Time"] = pd.to_datetime(df["Departure_Time"])
        df["Departure_Time"] = df["Departure_Time"].dt.date

        df["Return_Time"] = pd.to_datetime(df["Return_Time"])
        df["Return_Date"] = df["Return_Time"].dt.date

        for a, b, c, d, e, f, g, h in zip(
            df.Departure_Time,
            df.Return_Time,
            df.StationID,
            df.Departure_Station,
            df.Destination_StationID,
            df.Destination,
            df.Distance,
            df.Duration,
        ):
            models = Bike(
                departure_time=a,
                return_time=b,
                station_id=c,
                departure_station=d,
                destination_id=e,
                destination=f,
                distance=g,
                duration=h,
            )
            models.save()
