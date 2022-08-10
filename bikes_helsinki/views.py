from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Bike


class HomePageView(TemplateView):
    template_name = "home.html"


class SearchPageView(TemplateView):
    template_name = "search.html"


""" class BikeListView(ListView):
    model = Bike
    template_name = "datatable.html"
    context_object_name = "datatable" """


def datatable(request):
    qry = Bike.objects.all()
    departure_time = request.GET.get("departure_time")
    return_time = request.GET.get("return_time")
    departure_station = request.GET.get("departure_station")
    destination = request.GET.get("destination")
    station_id = request.GET.get("station_id")
    destination_id = request.GET.get("destination_id")
    distance = request.GET.get("distance")
    duration = request.GET.get("duration")

    if departure_station != "" and departure_station is not None:
        qry = qry.filter(departure_station__icontains=departure_station)

    elif station_id != "" and station_id is not None:
        qry = qry.filter(station_id=station_id)

    if destination != "" and destination is not None:
        qry = qry.filter(destination__icontains=destination)

    elif destination_id != "" and destination_id is not None:
        qry = qry.filter(destination_id=destination_id)

    context = {"queryset": qry}
    return render(request, "datatable.html", context)
