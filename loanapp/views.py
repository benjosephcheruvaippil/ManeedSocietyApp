import shutil
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from .models import FilesUpload,CarDetail
from django.conf import settings
import openpyxl
import os


# Create your views here.
def home_view(request):
    if request.method=="POST":
        # shutil.rmtree("..\\maneedsocietyapp\\media") #removes the directory media and all the files in it.
        shutil.rmtree(os.path.join(settings.BASE_DIR,'media')) #removes the directory media and all the files in it.
        filename=request.FILES["file"]
        print("filename",filename)
        document=FilesUpload.objects.create(file=filename)
        document.save()  #saves the file to media directory

        path=os.path.join(settings.BASE_DIR,'media/%s' %(filename))
        
        wb_obj=openpyxl.load_workbook(path)
        sheet_obj = wb_obj.active

        column_nos=sheet_obj.max_column
        row_nos=sheet_obj.max_row
        # dict_car={ }
        for r in range(row_nos):
            dict_car={ }
            for c in range(column_nos):
                if r!=0:
                    cell_obj = sheet_obj.cell(row = r+1, column = c+1)
                    if c+1==1:
                        dict_car['name']=cell_obj.value
                    if c+1==2:
                        dict_car['make']=cell_obj.value
                    if c+1==3:
                        dict_car['model']=cell_obj.value
            if r!=0:
                car_data=CarDetail.objects.create(
                    name=dict_car['name'],make=dict_car['make'],model=dict_car['model']
                )   
                print("Car Data",car_data)    

        # print("Cell value",cell_obj.value)
        # reading from excel

        return render(request,"loan-agreement.html")
    return render(request,"home-view.html")