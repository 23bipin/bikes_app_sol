from django.urls import path
from .views import (
    # BikeListView,
    HomePageView,
    SearchPageView,
    datatable,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # path("datatable/", BikeListView.as_view(), name="datatable"),
    path("datatable/", datatable, name="datatable"),
    path("search/", SearchPageView.as_view(), name="search"),
]
