from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group

def user_is_company(function):
    def wrap(request, *args, **kwargs):
        group = Group.objects.get(name='Компания')
        if group in request.user.groups.all() or request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
        
