import shutil
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from .models import FilesUpload,CarDetail
from django.conf import settings
import openpyxl
import os
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.views import View


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


# class ViewPDF(View):
#     def get(self,request,*args,**kwargs):
#         pdf=render_to_pdf("loan-agreement.html",loan_data)
#         return HttpResponse(pdf,content_type='application/pdf')
#         # return HttpResponse({"done"})

# def render_to_pdf(template_src,context_dict={}):
#     template=get_template(template_src)
#     html=template.render(context_dict)
#     result=BytesIO()
#     pdf=pisa.pisaDocument(BytesIO(html.encode("UTF-8")),result)
#     # pdf=pisa.CreatePDF(html,result,link_callback="",encoding='UTF-8')
#     if not pdf.err:
#         return HttpResponse(result.getvalue(),content_type='application/pdf')
#     return None

# def DownloadHTMLToPDF(request):
#     pdf=render_to_pdf("loan-agreement.html",loan_data)
#     response=HttpResponse(pdf,content_type='application/pdf')
#     filename="LoanAgreement_%s.pdf" %("00001")
#     content="attachment; filename=%s" %(filename)
#     response['Content-Disposition']=content
#     return response

def RenderHTML(request):
    print(request.POST.get('txtVaypa'))
    loan_data={
        "vaypanumber":request.POST.get('txtVaypa') if request.POST.get('txtVaypa')=="1" else "---" ,
        "thuka":request.POST.get('txtThuka'),
        "jamyam1":request.POST.get('txtJamyam1'),
        "jamyam2":request.POST.get('txtJamyam2'),
        "jamyam3":request.POST.get('txtJamyam3')
    }

    template=get_template("loan-agreement.html")
    html=template.render(loan_data)
    return HttpResponse(html)