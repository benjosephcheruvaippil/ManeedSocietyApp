
from loanapp.models import MemberDetails
from django.template.loader import get_template
from django.http import HttpResponse

def RenderHTML(request):
    # print(request.POST.get('txtVaypa'))
    # jamyam1_membernumber=request.POST.get('txtJamyam1')
    # jamyam2_membernumber=request.POST.get('txtJamyam2')
    # jamyam3_membernumber=request.POST.get('txtJamyam3')

    # jamyam1_name=""
    # jamyam1_taluk=""
    # jamyam1_village=""
    # jamyam1_kara=""
    # jamyam1_house=""
    # jamyam1_father_husband=""
    # jamyam1_age=""

    # getJamyam1Details=MemberDetails.objects.filter(member_number=jamyam1_membernumber).all()
    # for mem in getJamyam1Details:
    #     jamyam1_name=mem.name
    #     jamyam1_taluk=mem.taluk
    #     jamyam1_village=mem.village
    #     jamyam1_kara=mem.kara
    #     jamyam1_house=mem.house_name
    #     jamyam1_father_husband=mem.father_husband_name
    #     jamyam1_age=mem.age

    loan_data={
        # "vaypanumber":request.POST.get('txtVaypa') if request.POST.get('txtVaypa')!="" else "" ,
        # "thuka":request.POST.get('txtThuka') if request.POST.get('txtThuka')!="" else "",
        # "jamyam1":request.POST.get('txtJamyam1'),
        # "jamyam1_name":jamyam1_name,
        # "jamyam1_taluk":jamyam1_taluk,
        # "jamyam1_village":jamyam1_village,
        # "jamyam1_kara":jamyam1_kara,
        # "jamyam1_house":jamyam1_house,
        # "jamyam1_father_husband":jamyam1_father_husband,
        # "jamyam1_age":jamyam1_age,


        # "jamyam2":request.POST.get('txtJamyam2'),
        # "jamyam3":request.POST.get('txtJamyam3')
    }

    template=get_template("chitty-agreement.html")
    html=template.render(loan_data)
    return HttpResponse(html)