from django import template

register = template.Library()


@register.filter(name="float_percentage")
def float_percentage(value, arg):
    return round(value / arg * 100, 2)
