from django.http import HttpResponse
from django.core.exceptions import PermissionDenied


def check_session(some_func):
    def wrap(request):
        if request.session.has_key('username'):
            return some_func(request)
        else:
            raise PermissionDenied()
    return wrap