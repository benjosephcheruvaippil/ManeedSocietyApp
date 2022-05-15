
from loanapp.models import MemberDetails
from django.template.loader import get_template
from django.http import HttpResponse

def RenderHTML(request):
    print(request.POST.get('person_1'))
    mem_num_1=request.POST.get('person_1')
    mem_num_2=request.POST.get('person_2')
    mem_num_3=request.POST.get('person_3')
    mem_num_4=request.POST.get('person_4')

    person_1_name=""
    person_1_taluk=""
    person_1_village=""
    person_1_kara=""
    person_1_house=""
    person_1_father_husband=""
    person_1_age=""

    person_2_name=""
    person_2_taluk=""
    person_2_village=""
    person_2_kara=""
    person_2_house=""
    person_2_father_husband=""
    person_2_age=""

    person_3_name=""
    person_3_taluk=""
    person_3_village=""
    person_3_kara=""
    person_3_house=""
    person_3_father_husband=""
    person_3_age=""

    person_4_name=""
    person_4_taluk=""
    person_4_village=""
    person_4_kara=""
    person_4_house=""
    person_4_father_husband=""
    person_4_age=""

    get_Person_1_Details=MemberDetails.objects.filter(member_number=mem_num_1).all()
    for mem in get_Person_1_Details:
        person_1_name=mem.name
        person_1_taluk=mem.taluk
        person_1_village=mem.village
        person_1_kara=mem.kara
        person_1_house=mem.house_name
        person_1_father_husband=mem.father_husband_name
        person_1_age=mem.age
    
    get_Person_2_Details=MemberDetails.objects.filter(member_number=mem_num_2).all()
    for mem in get_Person_2_Details:
        person_2_name=mem.name
        person_2_taluk=mem.taluk
        person_2_village=mem.village
        person_2_kara=mem.kara
        person_2_house=mem.house_name
        person_2_father_husband=mem.father_husband_name
        person_2_age=mem.age
    
    get_Person_3_Details=MemberDetails.objects.filter(member_number=mem_num_3).all()
    for mem in get_Person_3_Details:
        person_3_name=mem.name
        person_3_taluk=mem.taluk
        person_3_village=mem.village
        person_3_kara=mem.kara
        person_3_house=mem.house_name
        person_3_father_husband=mem.father_husband_name
        person_3_age=mem.age
    
    get_Person_4_Details=MemberDetails.objects.filter(member_number=mem_num_4).all()
    for mem in get_Person_4_Details:
        person_4_name=mem.name
        person_4_taluk=mem.taluk
        person_4_village=mem.village
        person_4_kara=mem.kara
        person_4_house=mem.house_name
        person_4_father_husband=mem.father_husband_name
        person_4_age=mem.age

    loan_data={
        # "vaypanumber":request.POST.get('txtVaypa') if request.POST.get('txtVaypa')!="" else "" ,
        # "thuka":request.POST.get('txtThuka') if request.POST.get('txtThuka')!="" else "",
        # "jamyam1":request.POST.get('txtJamyam1'),
        "mem_num_1":mem_num_1,
        "person_1_name":person_1_name,
        "person_1_taluk":person_1_taluk,
        "person_1_village":person_1_village,
        "person_1_kara":person_1_kara,
        "person_1_house":person_1_house,
        "person_1_father_husband":person_1_father_husband,
        "person_1_age":person_1_age,

        "mem_num_2":mem_num_2,
        "person_2_name":person_2_name,
        "person_2_taluk":person_2_taluk,
        "person_2_village":person_2_village,
        "person_2_kara":person_2_kara,
        "person_2_house":person_2_house,
        "person_2_father_husband":person_2_father_husband,
        "person_2_age":person_2_age,

        "mem_num_3":mem_num_3,
        "person_3_name":person_3_name,
        "person_3_taluk":person_3_taluk,
        "person_3_village":person_3_village,
        "person_3_kara":person_3_kara,
        "person_3_house":person_3_house,
        "person_3_father_husband":person_3_father_husband,
        "person_3_age":person_3_age,

        "mem_num_4":mem_num_4,
        "person_4_name":person_4_name,
        "person_4_taluk":person_4_taluk,
        "person_4_village":person_4_village,
        "person_4_kara":person_4_kara,
        "person_4_house":person_4_house,
        "person_4_father_husband":person_4_father_husband,
        "person_4_age":person_4_age,
    }

    template=get_template("chitty-agreement.html")
    html=template.render(loan_data)
    return HttpResponse(html)