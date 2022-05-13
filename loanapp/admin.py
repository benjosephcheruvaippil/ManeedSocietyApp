import site
from django.contrib import admin
from django.apps import apps
from django.contrib.auth.models import User
from .models import FilesUpload,MemberDetails
# Register your models here.

models=apps.get_models()

admin.site.register(FilesUpload)
admin.site.register(MemberDetails)
# admin.site.register(admin.ModelAdmin)

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass