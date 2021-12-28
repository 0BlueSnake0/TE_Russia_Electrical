from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings   


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include("electrical.urls")), 
    path('accounts/', include("accounts.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)