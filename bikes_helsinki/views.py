from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Bike, StationDetails
from geopy.geocoders import Nominatim
from geopy import distance
import folium


class HomePageView(TemplateView):
    template_name = "home.html"


def datatable(request):
    qry = Bike.objects.all()
    departure_time = request.GET.get("departure_time")
    return_time = request.GET.get("return_time")
    departure_station = request.GET.get("departure_station")
    destination = request.GET.get("destination")
    station_id = request.GET.get("station_id")
    destination_id = request.GET.get("destination_id")
    distance_min = request.GET.get("distance_min")
    distance_max = request.GET.get("distance_max")
    duration_min = request.GET.get("duration_min")
    duration_max = request.GET.get("duration_max")
    duration = request.GET.get("duration")

    if departure_station != "" and departure_station is not None:
        qry = qry.filter(departure_station__icontains=departure_station)

    elif station_id != "" and station_id is not None:
        qry = qry.filter(station_id=station_id)

    if destination != "" and destination is not None:
        qry = qry.filter(destination__icontains=destination)

    elif destination_id != "" and destination_id is not None:
        qry = qry.filter(destination_id=destination_id)

    if distance_min != "" and distance_min is not None:
        qry = qry.filter(distance__gte=distance_min)

    if distance_max != "" and distance_max is not None:
        qry = qry.filter(distance__lt=distance_max)

    if duration_min != "" and duration_min is not None:
        qry = qry.filter(duration__gte=duration_min)

    if duration_max != "" and duration_max is not None:
        qry = qry.filter(duration__lt=duration_max)

    context = {"queryset": qry}
    return render(request, "datatable.html", context)


def search(request):
    qry = StationDetails.objects.all()

    x = request.GET.get("x")
    y = request.GET.get("y")
    # for map
    maps = folium.Map(location=[60.25, 24.80], zoom_start=10, control_scale=True)
    """ for index, lat in enumerate(x):
        folium.Marker([lat, y[index]]).add_to(maps) """
    # folium.RegularPolygonMarker(location=[x, y])
    # folium.Marker(location=float(x, y)).add_to(maps)
    # folium.LayerControl().add_to(maps)
    maps = maps._repr_html_()

    namn = request.GET.get("namn")
    if namn != "" and namn is not None and namn != "Select or Type":
        qry = qry.filter(namn=namn)

    context = {"queryset": qry, "maps": maps}
    return render(request, "search.html", context)
