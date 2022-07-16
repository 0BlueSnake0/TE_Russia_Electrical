from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.http import FileResponse
from xlsx2html import xlsx2html 
from .models import *

from .header import *
from .catalog import CATALOGS 
from .modals import MODALS
from .contacts import CONTACTS
from .product import PRODUCTS
from .department_info import DEPARTMENT_SPECIFICATIONS
from .slideshows import TEXT_SLIDESHOWS,IMAGE_SLIDESHOWS
from .tables import TABLES

from django.views.decorators.cache import never_cache


def index(request): 
    return render(
        request,
        template_name="electrical/index.html",
        context={
            'dropdown1':DROPDOWN_1,
            'department_specifications':DEPARTMENT_SPECIFICATIONS,
            'text_slideshows':TEXT_SLIDESHOWS,
            'image_slideshows':IMAGE_SLIDESHOWS,
            'intro_slideshow': [
                '/static/images/slideshow/machine.png',
                '/static/images/slideshow/man1.png',
                '/static/images/slideshow/man2.png',
                '/static/images/slideshow/robots.png',
                '/static/images/slideshow/surgeon.png',
            ],
            'under_header_content':"yes"
        }
    )   
    

def catalog(request, **kwargs):
    return render(
        request,
        template_name="electrical/catalog.html",
        context={
            'dropdown1':DROPDOWN_1,
            'catalogs':CATALOGS,
        }
    ) 


def catalog_detail(request, **kwargs):   
	filepath = f'{settings.BASE_DIR}/static/main/catalog_files/catalogs/{CATALOGS[kwargs["product"]]["category"]}/{CATALOGS[kwargs["product"]]["filename"]}'
	return FileResponse(
        open(filepath, 'rb'), 
        content_type='application/pdf'
    )


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


def product_detail(request, **kwargs):
    return render(
        request,
        template_name="electrical/product.html",
        context={ 
            'dropdown1':DROPDOWN_1,
            'product':PRODUCTS[kwargs["product_slug"]],
            'text_slideshows':TEXT_SLIDESHOWS,
            'image_slideshows':IMAGE_SLIDESHOWS,
            "modals":MODALS, 
        }
    ) 


def seminars_timetable(request, **kwargs):
    styles = TABLES["seminars_timetable"]["styles"]
    xlsx_path = f'{TABLES["seminars_timetable"]["xlsx_path"]}'
    html_path = f'{TABLES["seminars_timetable"]["html_path"]}'
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
        template_name=f'electrical/timetable.html',
        context={  
            'dropdown1':DROPDOWN_1,
            'table_path':html_path,
        }
    )  


def regions(request, **kwargs): 
    return render(
        request,
        template_name="electrical/regions.html",
        context={ 
            'dropdown1':DROPDOWN_1,
            "contacts":CONTACTS,
        }
    )  


def stop_activity(request, **kwargs): 
    return render(
        request,
        template_name="electrical/stop_activity.html"
    )  