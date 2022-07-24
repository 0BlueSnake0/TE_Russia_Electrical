from django.urls import path, include 
from .views import (
    index,
    CatalogListView, CatalogDetailView,
    ContactListView, RegionsView,
    ProductDetailView,
    seminars_timetable,
    stop_activity
)

app_name="electrical"
urlpatterns = [   
    path('', index, name="index"),
    path('catalogs/', CatalogListView.as_view(), name="catalogs"),
    path('catalogs/<slug:catalog_slug>/', CatalogDetailView.as_view(), name="catalog_detail"),
    path('contacts/<slug:city>/', ContactListView.as_view(), name="contacts"),
    path('regions/', RegionsView.as_view(), name="regions"),
    path('products/<slug:product_slug>/', ProductDetailView.as_view(), name="product_detail"),
    path('seminars_timetable/', seminars_timetable, name="seminars_timetable"),
    path('stop_activity/', stop_activity, name="stop_activity")
]
