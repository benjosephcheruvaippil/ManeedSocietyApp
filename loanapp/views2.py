
from loanapp.models import MemberDetails
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import date

def RenderHTML(request):
    print(request.POST.get('person_1'))
    mem_num_1=request.POST.get('person_1')
    mem_num_2=request.POST.get('person_2')
    mem_num_3=request.POST.get('person_3')
    mem_num_4=request.POST.get('person_4')

    todays_date=date.today()
    year_in_words=RetrieveYearAndMonth(todays_date.year)
    month_in_words=RetrieveYearAndMonth(todays_date.month)

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

    mds_no=request.POST.get('mds_no')
    monthly_instalment_amount=request.POST.get('monthly_instalment_amount')
    term=request.POST.get('term')
    total_amount=request.POST.get('total_amount')
    chittal_no=request.POST.get('chittal_no')
    auction_instalment_no=request.POST.get('auction_instalment_no')
    auction_date=request.POST.get('auction_date')
    less_called_amount=request.POST.get('less_called_amount')
    sro=request.POST.get('sro')
    land_document_no=request.POST.get('land_document_no')
    no_of_executants=request.POST.get('no_of_executants')
    date_of_instalment=request.POST.get('date_of_instalment')
    property_owner_specify_no=request.POST.get('property_owner_specify_no')
    district=request.POST.get('district')
    sub_district=request.POST.get('sub_district')
    taluk=request.POST.get('taluk')
    village=request.POST.get('village')
    kara=request.POST.get('kara')
    sy_no_and_sy_sub_division_no=request.POST.get('sy_no_and_sy_sub_division_no')
    re_sy_no=request.POST.get('re_sy_no')
    area=request.POST.get('area')

    txtbx1=mds_no
    txtbx2=monthly_instalment_amount
    txtbx3=term
    txtbx4=total_amount
    txtbx5=chittal_no
    txtbx6=auction_instalment_no
    txtbx7=auction_date
    txtbx8=total_amount
    txtbx9=less_called_amount
    txtbx10=total_amount-less_called_amount
    txtbx11="" #auction amount in words
    txtbx12=auction_instalment_no+1
    txtbx13=term
    txtbx14=term-auction_instalment_no
    txtbx15=monthly_instalment_amount
    txtbx16=monthly_instalment_amount*txtbx14
    txtbx17="" #total remaining amount in words
    txtbx18=sro
    txtbx19=land_document_no
    txtbx20="" #village
    txtbx21=sy_no_and_sy_sub_division_no
    txtbx22=area
    txtbx23=no_of_executants
    txtbx24=monthly_instalment_amount
    txtbx25=no_of_executants
    txtbx26=no_of_executants
    txtbx27=no_of_executants
    txtbx28=date_of_instalment
    txtbx29=monthly_instalment_amount*txtbx14
    txtbx30="" #total remaining amount in words
    txtbx31=monthly_instalment_amount
    txtbx32=term-auction_instalment_no
    txtbx33=no_of_executants
    txtbx34=no_of_executants
    txtbx35=property_owner_specify_no
    txtbx36="" #village
    txtbx37=sro
    txtbx38=land_document_no
    txtbx39=district
    txtbx40=sub_district
    txtbx41=taluk
    txtbx42=village
    txtbx43=kara
    txtbx44=sy_no_and_sy_sub_division_no
    txtbx45=re_sy_no
    txtbx46=area
    txtbx47="" #village
    txtbx48=sy_no_and_sy_sub_division_no
    txtbx49=area



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
        "year_in_words":year_in_words,
        "month_in_words":month_in_words,

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



def RetrieveYearAndMonth(val):
    year_month_dict={
        2022:"Two Thousand Twenty Two",
        2023:"Two Thousand Twenty Three",
        2024:"Two Thousand Twenty Four",
        2025:"Two Thousand Twenty Five",
        2026:"Two Thousand Twenty Six",
        2027:"Two Thousand Twenty Seven",
        2028:"Two Thousand Twenty Eight",
        2029:"Two Thousand Twenty Nine",
        2030:"Two Thousand Twenty Thirty",
        2031:"Two Thousand Thirty One",
        2032:"Two Thousand Thirty Two",
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December",
    }

    return year_month_dict[val]