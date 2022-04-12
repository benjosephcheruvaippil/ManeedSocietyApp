import site
from django.contrib import admin
from .models import FilesUpload,CarDetail
# Register your models here.

admin.site.register(FilesUpload)
admin.site.register(CarDetail)
