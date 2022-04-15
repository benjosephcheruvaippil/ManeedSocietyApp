from django import views
from django.urls import path,include
from .views import home_view,RenderHTML
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home-view',views.home_view,name='home-view'),
    # path('download-loan-agreement',views.DownloadHTMLToPDF,name='download-loan-agreement'),
    # path('view-pdf',views.ViewPDF.as_view(),name='view-pdf'),
    path('render-loan-agreement',views.RenderHTML,name='render-loan-agreement'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)