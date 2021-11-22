from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.http import FileResponse
from .catalog import CATALOGS
from .models import *
from .header import *


def index(request):
    return render(
        request,
        template_name="electrical/index.html",
        context={
            'dropdown1':DROPDOWN_1,
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
	filepath = f'{settings.BASE_DIR}/static/main/catalog_files/{kwargs["folder"]}/{CATALOGS[kwargs["folder"]]["filename"]}'
	return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def contacts(request, **kwargs):
    
    return render(
        request,
        template_name="electrical/contacts.html",
        context={
            'dropdown1':DROPDOWN_1,
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