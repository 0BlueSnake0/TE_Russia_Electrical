from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.http import FileResponse
from .catalog import CATALOGS
from .contacts import CONTACTS
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


def category(request, **kwargs):
    return HttpResponse("")


def technologies(request, **kwargs):
    return HttpResponse("")
    

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
    
    return render(
        request,
        template_name="electrical/contacts.html",
        context={
            'dropdown1':DROPDOWN_1,
            "contacts":CONTACTS,
            "current_city":kwargs["city"],
        }
    )



def video_list(request, **kwargs):
    # This view shows page with all videos related with current category
    all_videos = Video.objects.all()
    return render(
        request,
        template_name="electrical/video_list.html",
        context={
            "all_videos":all_videos,
        }
    )

def detail_video(request, **kwargs):
    # This view shows detail page of one video
    video = Video.objects.get(slug=kwargs["video_slug"])
    return render(
        request,
        template_name="electrical/video_detail.html",
        context={"video":video}
    )