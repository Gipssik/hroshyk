from django import template

register = template.Library()


@register.simple_tag()
def format_string(element, **kwargs):
    return element.format(**kwargs)
