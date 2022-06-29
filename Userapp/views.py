
from imaplib import _Authenticator
from django.shortcuts import redirect, render
from Adminapp.models import Detaildb
from Userapp.models import ContactForJoinDb, Contactdb, RegisterDb
from Adminapp.models import Detaildb
from django.contrib.auth.models import User
# Create your views here.
def Userpage(request):
    obj=Detaildb.objects.all()
    return render(request,'user.html',{'obj':obj})

def Aboutpage(request):
    return render(request,'about.html')    

def Destinationpage(request):
    return render(request,'travel_destination.html')

def DestinationDetails(request):
    return render(request,'destination_details.html')    

def ContactPage(request):
    return render(request,'contact.html')    

def Getcontactdata(request):
    print('is in contact send')
    if (request.method=='POST'):
        n_name=request.POST.get('name')
        n_message=request.POST.get('message')
        n_email=request.POST.get('email')
        n_subject=request.POST.get('subject')
        n_data=Contactdb(name=n_name,message=n_message,email=n_email,subject=n_subject)
        n_data.save()
    return redirect(Userpage)

def RegisterPage(request):
       return render(request,'register.html')


def RegisterData(request):
    if(request.method=='POST'):
        m_username=request.POST.get('Username')
        m_email=request.POST.get('email')       
        m_password=request.POST.get('password')
        m_data=RegisterDb(Username=m_username,email=m_email,password=m_password)
        m_data.save()
    return redirect(LoginPage)     

def LoginPage(request):
    return render(request,'login.html')    
def LoginData(request):
    m_username=request.POST.get('Username')
    m_password=request.POST.get('password')
    if RegisterDb.objects.filter(Username=m_username,password=m_password).exists():
        m_data=RegisterDb.objects.filter(Username=m_username,password=m_password).values('email','id').first()
        request.session['email']=m_data['email']
        request.session['userid']=m_data['id']
        request.session['password']=m_password
        request.session['Username']=m_username
        
        return redirect(Userpage)
    else:
        return redirect(RegisterPage)

        
def LogOut(request):
    del request.session['Username']
    del request.session['password']
    

    return redirect(RegisterPage)

def ContactJoinData(request):
    if request.method=='POST':
        b_name=request.POST.get('name')
        b_message=request.POST.get('message')
        b_phone=request.POST.get('phone')

        b_data=ContactForJoinDb(name=b_name,message=b_message,phone=b_phone)
        b_data.save()
    return redirect(Userpage)

    