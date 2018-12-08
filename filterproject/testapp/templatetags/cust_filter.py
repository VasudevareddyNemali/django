from django import template
register=template.Library()

def truncate3(value):
    result=value[0:5]
    return result


@register.filter(name='truncate_n')
def truncate_n(value,n):
    result=value[0:n]
    return 'Bujjigadu'
