from django.urls import path, include 
from .views import * 

app_name="electrical"
urlpatterns = [  
    path('<slug:category_slug>/', category, name="category"),
    path('<slug:category_slug>/technologies', technologies, name="technologies"),
    path('<slug:category_slug>/catalog', catalog, name="catalog"),
    path('<slug:category_slug>/videos', videos, name="videos"),
]