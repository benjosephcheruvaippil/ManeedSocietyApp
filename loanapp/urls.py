from django import views
from django.urls import path,include
from .views import home_view,DownloadHTMLToPDF,ViewPDF,RenderHTML
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home-view',views.home_view,name='home-view'),
    path('download-loan-agreement',views.DownloadHTMLToPDF,name='download-loan-agreement'),
    path('view-pdf',views.ViewPDF.as_view(),name='view-pdf'),
    path('render-html',views.RenderHTML,name='render-html'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)