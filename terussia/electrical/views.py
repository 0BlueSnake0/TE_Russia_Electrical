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
            'image_slideshow': [
                '/static/images/slideshow/machine.png',
                '/static/images/slideshow/man1.png',
                '/static/images/slideshow/man2.png',
                '/static/images/slideshow/robots.png',
                '/static/images/slideshow/surgeon.png',
            ],
            'text_slideshow': {
                0: {
                    "title":"ПРОДУКЦИЯ НА СКЛАДЕ В РОССИИ",
                    "text":"""
                        Локализация склада в Москве позволяет осуществлять 
                        отгрузки продукции буквально на следующий день после размещения заказа
                    """,
                },
                1: { 
                    "title":"ОБУЧАЮЩИЕ ЦЕНТРЫ В РОССИИ",
                    "text":"""
                        Тайко Электроникс РУС – это 2 крупных центра ТЕХНИЧЕСКОЙ  
                        поддержки клиентов в Москве и Санкт-Петербурге, которые занимаются 
                        консультацией, обучением инженерно-технического персонала, руководителей 
                        организаций, сотрудников офисов продаж, конечных заказчиков  по вопросам 
                        характеристик и применения оборудования, произведенного на заводах 
                        TE connectivity
                    """, 
                },
                2: { 
                    "title":"СЕТЬ ДИСТРИБЬЮТОРОВ",
                    "text":"""
                        Разветвленная сеть дистрибьюторских центров насчитывает более 50 
                        крупных организаций по всей территории РФ, что позволяет
                        в оперативном порядке найти продукцию TE в наличии в любом регионе.
                    """, 
                },
                3: { 
                    "title":"ПРЕДСТАВИТЕЛЬСТВА В РЕГИОНАХ",
                    "text":"""
                        Офисы “Тайко Электроникс РУС” представлены в основных 
                        крупных регионах России, в городах: Москва, Санкт-Петербург и  
                        Екатеринбург. 
                    """, 
                }, 
            },
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