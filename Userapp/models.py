import email
from unicodedata import name
from django.db import models

# Create your models here.
class Contactdb(models.Model):
    message=models.CharField( max_length=500,null=True,blank=False)
    name=models.CharField(max_length=200,null=True,blank=False)
    email=models.CharField(max_length=200,null=True,blank=False)
    subject=models.CharField(max_length=200,null=True,blank=False)
class RegisterDb(models.Model):
    Username=models.CharField(max_length=200,null=True,blank=False)
    password=models.CharField(max_length=200,null=True,blank=False)
    email=models.CharField(max_length=200,null=True,blank=False)

class ContactForJoinDb(models.Model):
    name=models.CharField(max_length=200,null=True,blank=False)
    phone=models.IntegerField(null=True,blank=False)
    message=models.CharField(max_length=200,null=True,blank=False)
