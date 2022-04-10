from django import views
from django.urls import path,include
from .views import home_view
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home-view',views.home_view,name='home-view')
]

if settings.DEBUG:
    # urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)