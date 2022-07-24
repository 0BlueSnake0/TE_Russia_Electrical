from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings   


class RedirectMiddleware: 
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request): 
        url = request.get_full_path()
        if (not settings.STOP_ACTIVITY) and ('terussia.ru' in url or 'bluesnakeengineer.ru' in url):
            return redirect(f'/electrical/{request.path}')
        return self.get_response(request)
