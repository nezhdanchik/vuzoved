from django import template

register = template.Library()


@register.filter
def replace(value, arg):
    """Принимает строку, содержащую 2 аргумента через запятую"""
    a, b = arg.split(',')
    return value.replace(a, b)
