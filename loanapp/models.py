from datetime import date
from django.db import models

# Create your models here.
class FilesUpload(models.Model):
    file=models.FileField()


class MemberDetails(models.Model):
    member_number=models.IntegerField(default=0)
    member_type=models.CharField(null=True,max_length=2,default="")
    name=models.CharField(null=True,max_length=301,default="")
    sex=models.CharField(null=True,max_length=3,default="")
    father_husband_name=models.CharField(null=True,max_length=300,default="")
    house_name=models.CharField(null=True,max_length=700,default="")
    kara=models.CharField(null=True,max_length=700,default="")
    post=models.CharField(null=True,max_length=300,default="")
    pin=models.CharField(null=True,max_length=300,default="")
    village=models.CharField(null=True,max_length=300,default="")
    taluk=models.CharField(null=True,max_length=300,default="")
    panchayath=models.CharField(null=True,max_length=300,default="")
    ward=models.CharField(null=True,max_length=300,default="")
    mobile_number=models.CharField(null=True,max_length=300,default="")
    dob=models.DateField(null=True,default=date.today)
    age=models.IntegerField(null=True,default=0)
    aadhar=models.CharField(null=True,max_length=300,default="")
    occupation=models.CharField(null=True,max_length=300,default="")