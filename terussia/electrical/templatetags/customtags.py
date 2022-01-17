from django import template
from django.core.exceptions import ObjectDoesNotExist
from ..models import *
import random
register = template.Library()


@register.simple_tag
def get_range(number):
    return list(range(number))


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def get_first_item(dictionary):
    values_view = dictionary.values()
    value_iterator = iter(values_view)
    first_value = next(value_iterator)
    return first_value

@register.simple_tag
def get_random_num(): 
    return random.random() 