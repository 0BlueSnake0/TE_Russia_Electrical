from ..states import STATES
from ..models import State, Region
from django.conf import settings   


class InitStatesMiddleware: 
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request): 
        for region_color in STATES:
            for (name, slug) in STATES[region_color]:
                if not State.objects.filter(slug=slug).exists():
                    state = State.objects.create(slug=slug, name=name) 
                    if Region.objects.filter(color=region_color).exists(): 
                        state.region = Region.objects.get(color=region_color)
                        state.save()

        return self.get_response(request)