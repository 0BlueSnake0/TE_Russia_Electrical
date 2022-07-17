from ..states import STATES
from ..models import State
from django.conf import settings   


class StateAdminMiddleware: 
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request): 
        for (slug, name) in STATES:
            if not State.objects.filter(slug=slug).exists():
                State.objects.create(
                    slug=slug,
                    name=name
                )
            else:
                print((slug, name), "exist!")