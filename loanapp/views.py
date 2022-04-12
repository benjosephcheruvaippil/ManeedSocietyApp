import shutil
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from .models import FilesUpload
from django.conf import settings
import openpyxl
import os


# Create your views here.
def home_view(request):
    if request.method=="POST":
        # shutil.rmtree("..\\maneedsocietyapp\\media") #removes the directory media and all the files in it.
        filename=request.FILES["file"]
        print("filename",filename)
        document=FilesUpload.objects.create(file=filename)
        document.save()  #saves the file to media directory

        # reading from excel
        # path="..\\maneedsocietyapp\\media\\%s" %(filename)
        path=os.path.join(settings.BASE_DIR,'staticfiles/%s' %(filename))
        print("path",path)
        
        wb_obj=openpyxl.load_workbook(path)
        sheet_obj = wb_obj.active
        cell_obj = sheet_obj.cell(row = 2, column = 1)
        print("Cell value",cell_obj.value)
        # reading from excel

        return HttpResponse("Your file was saved successfully"+"-"+"Cell Value:"+cell_obj.value+".Filename: "+str(filename))
    return render(request,"home-view.html")