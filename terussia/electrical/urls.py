from django.urls import path, include 
from .views import * 

app_name="electrical"
urlpatterns = [   
    path('', index, name="index"),
    path('catalog/', catalog, name="catalog"),
    path('catalog/<slug:product>/', catalog_detail, name="catalog_detail"),
    path('contacts/<slug:city>/', contacts, name="contacts"),
    path('<slug:category_slug>/videos', video_list, name="videos"),
    path('<slug:category_slug>/videos/(?P<video_slug>\w+)', detail_video, name="detail_video"),
]