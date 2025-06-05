from django import template

register = template.Library()

@register.filter(name="swap")
def swap(value):
    return value.replace(" ","-")
