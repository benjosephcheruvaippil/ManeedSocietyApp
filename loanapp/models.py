from django.db import models

# Create your models here.
class FilesUpload(models.Model):
    file=models.FileField()

class CarDetail(models.Model):
    name=models.CharField(max_length=200)
    make=models.CharField(max_length=200)
    model=models.CharField(max_length=200)