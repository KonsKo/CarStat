from django import template

register = template.Library()

@register.filter(name='get_one')
def get_one(l, index):
    return l[index-1]