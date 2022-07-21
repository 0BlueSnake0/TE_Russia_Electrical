from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.http import FileResponse
from xlsx2html import xlsx2html 
from pytils.translit import slugify 
from .models import *

from .catalog import CATALOGS 
from .modals import MODALS


def index(request): 
    return render(
        request,
        template_name="electrical/index.html",
        context={
            'image_slideshow': [
                '/static/images/slideshow/robots.png',
                '/static/images/slideshow/man1.png',
                '/static/images/slideshow/man2.png',
                '/static/images/slideshow/surgeon.png',
                '/static/images/slideshow/machine.png',
            ],
            'text_slideshow': {
                0: {
                    "title":"Продукция на складе в Росии",
                    "text":"""
                        Локализация склада в Москве позволяет осуществлять 
                        отгрузки продукции буквально на следующий день после размещения заказа
                    """,
                },
                1: { 
                    "title":"Обучающие центры в России",
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
                    "title":"Сеть дистрибьюторов",
                    "text":"""
                        Разветвленная сеть дистрибьюторских центров насчитывает более 50 
                        крупных организаций по всей территории РФ, что позволяет
                        в оперативном порядке найти продукцию TE в наличии в любом регионе.
                    """, 
                },
                3: { 
                    "title":"Представительства в регионах",
                    "text":"""
                        Офисы “Тайко Электроникс РУС” представлены в основных 
                        крупных регионах России, в городах: Москва, Санкт-Петербург и  
                        Екатеринбург. 
                    """, 
                }, 
            }
        }
    )   
    

def catalogs(request):
    return render(
        request,
        template_name="electrical/catalogs.html",
        context={
            'catalogs':list(Catalog.objects.all()),
        }
    ) 


def catalog_detail(request, **kwargs):   
    pdf_file = f'{settings.BASE_DIR}{Catalog.objects.get(slug=kwargs["catalog_slug"]).pdf.url}'
    return FileResponse(open(pdf_file, 'rb'), content_type='application/pdf' )


def contacts(request, **kwargs):
    contacts_dict = {}
    for contact in list(ContactPerson.objects.all()):
        slugified_city = slugify(contact.city)
        if slugified_city not in contacts_dict:
            contacts_dict[slugified_city] = []
        contacts_dict[slugified_city].append(contact)

    return render(
        request,
        template_name="electrical/contacts.html",
        context={
            "current_city":kwargs["city"],
            "contacts":contacts_dict[kwargs["city"]]
        }
    )


def product_detail(request, **kwargs): 
    return render(
        request,
        template_name="electrical/product.html",
        context={  
            'product': Product.objects.get(slug=kwargs['product_slug']) 
        }
    ) 


def seminars_timetable(request, **kwargs):
    try:
        timetable = list(TimeTable.objects.all())[0]
        table_path = f'{settings.BASE_DIR}{timetable.table.url}'
        html_path = f'{settings.BASE_DIR}/electrical/templates/electrical/timetable_file.html'
    
        xlsx2html(table_path, html_path) 
        
        file = open(html_path, 'r', encoding="utf8")  
        html = f"""
            <link rel="stylesheet" type="text/css" href="/static/css/timetable.css"> 
            {file.read()}
        """
        file.close() 

        file = open(html_path, 'w',encoding='utf8')
        file.write(html)
        file.close() 
    except (FileNotFoundError, IndexError):
        html_path = ''
    
    return render(
        request,
        template_name=f'electrical/timetable.html',
        context={   
            'html_table_path':html_path,
        }
    )  


def regions(request):    
    contacts_dict = {}
    for contact in list(ContactPerson.objects.all()):
        slugified_city = slugify(contact.city)
        if slugified_city not in contacts_dict:
            contacts_dict[slugified_city] = []
        contacts_dict[slugified_city].append(contact)

    return render(
        request,
        template_name="electrical/regions.html",
        context={  
            "contacts":contacts_dict,
        }
    )  


def stop_activity(request, **kwargs): 
    return render(
        request,
        template_name="electrical/stop_activity.html"
    )  
