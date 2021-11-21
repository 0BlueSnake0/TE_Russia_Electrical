from django import template
register = template.Library()


@register.simple_tag
def get_range(number):
    return list(range(number))