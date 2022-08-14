from django.core.management.base import BaseCommand
import pandas as pd
from bikes_helsinki.models import StationDetails
from geopy.geocoders import Nominatim
from geopy import distance
import folium


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        df = pd.read_csv("static/data/station-details.csv")
        df = df.round(decimals=2)

        for aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm in zip(
            df.FID,
            df.ID,
            df.Nimi,
            df.Namn,
            df.Name,
            df.Osoite,
            df.Adress,
            df.Kaupunki,
            df.Stad,
            df.Operaattor,
            df.Kapasiteet,
            df.x,
            df.y,
        ):
            stationdetails = StationDetails(
                fid=aa,
                id=bb,
                nimi=cc,
                namn=dd,
                name=ee,
                osoite=ff,
                adress=gg,
                kaupunki=hh,
                stad=ii,
                operaator=jj,
                capacity=kk,
                x=ll,
                y=mm,
            )
            stationdetails.save()
