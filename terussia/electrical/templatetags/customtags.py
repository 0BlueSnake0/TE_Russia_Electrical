from django import template
from django.core.exceptions import ObjectDoesNotExist
from ..models import Product, ContactPerson
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
def get_item_index(lst, item):
    return list(lst).index(item)


@register.simple_tag
def get_dictitem_content(item):
    return item[1]


@register.simple_tag
def get_products():
    return sorted(list(Product.objects.all()), key=lambda product: product.order, reverse=True)


@register.simple_tag
def get_contacts():
    contacts = []
    for person in ContactPerson.objects.all():
        if person.city not in contacts:
            contacts += [person.city]  
    return contacts