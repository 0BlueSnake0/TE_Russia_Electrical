from django.urls import path, include 
from .views import * 

app_name="electrical"
urlpatterns = [   
    path('', index, name="index"),
    path('catalogs/', catalogs, name="catalogs"),
    path('catalogs/<slug:catalog_slug>/', catalog_detail, name="catalog_detail"),
    path('contacts/<slug:city>/', contacts, name="contacts"),
    path('regions/', regions, name="regions"), 
    path('products/<slug:product_slug>/', product_detail, name="product_detail"),
    path('seminars_timetable/', seminars_timetable, name="seminars_timetable"),
    path('stop_activity/', stop_activity, name="stop_activity")
]