from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings   
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('administration/', admin.site.urls),  
    path('', include("electrical.urls")), 
    path('accounts/', include("accounts.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns() 