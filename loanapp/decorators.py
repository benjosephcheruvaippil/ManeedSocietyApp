from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

def check_session(request):
    def decorator(some_func):
        def wrap(self,request,*args,**kwargs):
            if request.session.has_key('username'):
                return some_func(self,request,*args,**kwargs)
            else:
                raise PermissionDenied()
        return wrap
    return decorator