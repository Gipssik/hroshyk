from django import template

register = template.Library()


@register.filter(name="curled_format")
def curled_format(value, arg):
    return value.format(arg)
