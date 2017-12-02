from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='is_company')
def is_company(user):
    group = Group.objects.get(name='Компания')
    return group in user.groups.all() or user.is_staff
