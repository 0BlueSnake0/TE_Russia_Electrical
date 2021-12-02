from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.http import FileResponse
from .catalog import CATALOGS
from .contacts import CONTACTS
from .product import PRODUCTS
from .department_info import DEPARTMENT_SPECIFICATIONS
from .slideshows import TEXT_SLIDESHOWS,IMAGE_SLIDESHOWS
from .models import *
from .header import *


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
	filepath = f'{settings.BASE_DIR}/static/main/catalog_files/catalogs/{CATALOGS[kwargs["product"]]["filename"]}'
	return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


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


def regions(request, **kwargs):
    return render(
        request,
        template_name="electrical/regions.html",
        context={ 
            'dropdown1':DROPDOWN_1,
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
        }
    )


def timetable(request, **kwargs):
    return render(
        request,
        template_name="electrical/timetable.html",
        context={  
        }
    )


def video_list(request, **kwargs): 
    all_videos = Video.objects.all()
    return render(
        request,
        template_name="electrical/video_list.html",
        context={
            "all_videos":all_videos,
        }
    )

def detail_video(request, **kwargs): 
    video = Video.objects.get(slug=kwargs["video_slug"])
    return render(
        request,
        template_name="electrical/video_detail.html",
        context={"video":video}
    )

