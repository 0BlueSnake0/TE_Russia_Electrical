from django.shortcuts import render, HttpResponse
from .models import *


def index(request):
    return render(
        request,
        template_name="electrical/index.html",
        context={}
    )


def category(request, **kwargs):
    return HttpResponse("")


def technologies(request, **kwargs):
    return HttpResponse("")
    

def catalog(request, **kwargs):
    return HttpResponse("")


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