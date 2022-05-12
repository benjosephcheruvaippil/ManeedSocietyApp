from django.db import models

# Create your models here.
class FilesUpload(models.Model):
    file=models.FileField()

class CarDetail(models.Model):
    name=models.CharField(max_length=200)
    make=models.CharField(max_length=200)
    model=models.CharField(max_length=200)

class MemberDetails(models.Model):
    member_number=models.IntegerField
    member_type=models.CharField
    name=models.CharField(max_length=300)
    sex=models.CharField
    father_husband_name=models.CharField
    house_name=models.CharField
    kara=models.CharField
    post=models.CharField
    pin=models.CharField
    village=models.CharField
    taluk=models.CharField
    panchayath=models.CharField
    ward=models.CharField
    mobile_number=models.CharField
    dob=models.DateField
    age=models.IntegerField
    aadhar=models.CharField