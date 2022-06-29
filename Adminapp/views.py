
import email
from pyexpat import model
from urllib import request
from django.shortcuts import redirect, render
from Adminapp.models import Detaildb
from Userapp import views
from Userapp.models import Contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from Userapp.models import Contactdb



# Create your views here.
def index(request):
    return render(request,'index.html')

def addIndexPage(request):
    return render(request,'addPlaces.html')  

    
def getdata(request):
    if request.method == "POST":
        m_img=request.FILES['abc']
        m_destination=request.POST.get('destinationName')
        m_loacation=request.POST.get('locationName')
        m_price=request.POST.get('price')
        data=Detaildb(destinationName=m_destination,locationName=m_loacation,price=m_price,abc=m_img)
        data.save()
    return redirect(tablePage) 
def tablePage(request):
    obj=Detaildb.objects.all()
    return render(request,'tables.html',{'obj':obj})       
def ViewContactTable(request):
    obj=Contactdb.objects.all()
    return render(request,'contactTable.html',{'obj':obj})
def AdminLogin(request):
    return render(request,'adminlogin.html')
def getlogin(request):
    m_username=request.POST.get('Username')
    m_password=request.POST.get('password')

    if User.objects.filter(username__contains=m_username).exists():
        user=authenticate(username=m_username,password=m_password)
        if user is not None:
            login(request,user)
            request.session['username']=m_username
            request.session['password']=m_password

            return redirect(index)
        else:
            return redirect(AdminLogin)
    else:
        return redirect(AdminLogin)            


    