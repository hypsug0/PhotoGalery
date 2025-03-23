from django import template

register = template.Library()


@register.filter
def underscore_to_space(value):
    """Replace underscore to space"""
    return value.replace("_", " ")
