from django.shortcuts import render, HttpResponse


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

def videos(request, **kwargs):
    return HttpResponse("")