from django import template
from django.core.exceptions import ObjectDoesNotExist
from ..models import Product, ContactPerson, Region, State
from pytils.translit import slugify 

register = template.Library() 


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


@register.simple_tag
def get_states(region):
    return list(State.objects.filter(region=region))

@register.simple_tag
def slugify_word(word):
    return slugify(word)