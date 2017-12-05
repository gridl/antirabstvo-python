from django.core.exceptions import PermissionDenied

def user_is_employer(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_employer or request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
        
