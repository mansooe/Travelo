from distutils.command.upload import upload
import email
from pyexpat import model
from urllib import request
from django.db import models

# Create your models here.
class Detaildb(models.Model):
    abc=models.ImageField(upload_to='media',null=True,blank=False)
    destinationName=models.CharField(max_length=200,null=True,blank=False)
    locationName=models.CharField(max_length=200,null=True,blank=False)
    price=models.IntegerField(null=True,blank=False)
