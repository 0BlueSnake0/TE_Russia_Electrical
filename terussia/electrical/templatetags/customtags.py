from django import template
register = template.Library()


@register.simple_tag
def get_range(number):
    return list(range(number))


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)