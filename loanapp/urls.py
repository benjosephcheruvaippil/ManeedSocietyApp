from django import views
from django.urls import path,include
from loanapp.authentication import login,logout
from loanapp.views import home_view,RenderHTML
from . import authentication
from . import views
from . import views2

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home-view',views.home_view,name='home-view'),
    path('',authentication.login,name=''),
    path('logout',authentication.logout,name='logout'),
    path('render-loan-agreement',views.RenderHTML,name='render-loan-agreement'),
    path('render-chitty-agreement',views2.RenderHTML,name='render-chitty-agreement'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)