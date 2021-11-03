 
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 
from catalog.views import index


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', index),
    path('catalog/', include("catalog.urls")),
    path('accounts/', include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)