from django.urls import path, include 
from .views import * 

app_name="electrical"
urlpatterns = [   
    path('', index, name="index"),
    path('catalog/', catalog, name="catalog"),
    path('catalog/<slug:product>/', catalog_detail, name="catalog_detail"),
    path('contacts/<slug:city>/', contacts, name="contacts"),
    path('regions/<slug:region_slug>', regions, name="regions"), 
    path('products/<slug:product_slug>/', product_detail, name="product_detail"),
    path('seminars_timetable/', seminars_timetable, name="seminars_timetable")
]