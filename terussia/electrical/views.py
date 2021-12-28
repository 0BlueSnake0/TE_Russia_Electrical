from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.http import FileResponse
from xlsx2html import xlsx2html 
from .models import *

from .header import *
from .catalog import CATALOGS
from .contacts import CONTACTS
from .product import PRODUCTS
from .department_info import DEPARTMENT_SPECIFICATIONS
from .slideshows import TEXT_SLIDESHOWS,IMAGE_SLIDESHOWS
from .tables import TABLES

from django.views.decorators.cache import never_cache

@never_cache
def index(request): 
    return render(
        request,
        template_name="electrical/index.html",
        context={
            'dropdown1':DROPDOWN_1,
            'department_specifications':DEPARTMENT_SPECIFICATIONS,
            'text_slideshows':TEXT_SLIDESHOWS,
            'image_slideshows':IMAGE_SLIDESHOWS,
        }
    )   
    
@never_cache
def catalog(request, **kwargs):
    return render(
        request,
        template_name="electrical/catalog.html",
        context={
            'dropdown1':DROPDOWN_1,
            'catalogs':CATALOGS,
        }
    ) 

@never_cache
def catalog_detail(request, **kwargs):   
	filepath = f'{settings.BASE_DIR}/static/main/catalog_files/catalogs/{CATALOGS[kwargs["product"]]["filename"]}'
	return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

@never_cache
def contacts(request, **kwargs):
    print("you see regions now!")
    return render(
        request,
        template_name="electrical/contacts.html",
        context={
            'dropdown1':DROPDOWN_1,
            "contacts":CONTACTS,
            "current_city":kwargs["city"],
        }
    )

@never_cache
def product_detail(request, **kwargs):
    return render(
        request,
        template_name="electrical/product.html",
        context={ 
            'dropdown1':DROPDOWN_1,
            'product':PRODUCTS[kwargs["product_slug"]],
            'text_slideshows':TEXT_SLIDESHOWS,
            'image_slideshows':IMAGE_SLIDESHOWS,
        }
    ) 
@never_cache
def seminars_timetable(request, **kwargs):
    styles = TABLES["timetable_2020"]["styles"]
    xlsx_path = f'{TABLES["timetable_2020"]["xlsx_path"]}'
    html_path = f'{TABLES["timetable_2020"]["html_path"]}'
    xlsx2html(xlsx_path, html_path) 
    
    file = open(html_path, 'r', encoding="utf8")
    table = file.read()
    html = f'{styles}\n{table}'
    file.close() 

    file = open(html_path, 'w',encoding='utf8')
    file.write(html)
    file.close()
    

    return render(
        request,
        template_name="electrical/timetable.html",
        context={  
            'dropdown1':DROPDOWN_1,
        }
    )



@never_cache
def regions(request, **kwargs):
    map = ""
    return render(
        request,
        template_name="electrical/regions.html",
        context={ 
            'dropdown1':DROPDOWN_1,
            "contacts":CONTACTS,
        }
    )

@never_cache
def video_list(request, **kwargs): 
    all_videos = Video.objects.all()
    return render(
        request,
        template_name="electrical/video_list.html",
        context={
            "all_videos":all_videos,
        }
    )
@never_cache
def detail_video(request, **kwargs): 
    video = Video.objects.get(slug=kwargs["video_slug"])
    return render(
        request,
        template_name="electrical/video_detail.html",
        context={"video":video}
    )

