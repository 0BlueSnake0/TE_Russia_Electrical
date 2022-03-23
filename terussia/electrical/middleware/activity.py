from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings   

class StopActivityMiddleware: 
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request): 
        if (settings.STOP_ACTIVITY) and ('stop_activity' not in request.path) :
            return redirect("/electrical/stop_activity")
        return self.get_response(request)