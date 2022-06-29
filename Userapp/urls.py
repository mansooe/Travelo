from django.urls import path

import Adminapp
from.import views
urlpatterns = [
    path('Userpage',views.Userpage,name='Userpage'),
    path("Aboutpage", views.Aboutpage, name="Aboutpage"),
    path("Destinationpage",views.Destinationpage,name='Destinationpage'),
    path('DestinationDetails',views.DestinationDetails,name='DestinationDetails'),
    path('ContactPage',views.ContactPage,name='ContactPage'),
    path('Getcontactdata',views.Getcontactdata,name='Getcontactdata'),
    path('RegisterPage',views.RegisterPage,name='RegisterPage'),
    path('RegisterData',views.RegisterData,name='RegisterData'),
    path('',views.LoginPage,name="LoginPage"),
    path('LoginData',views.LoginData,name='LoginData'),
    path('LogOut',views.LogOut,name="LogOut"),
    path('ContactJoinData',views.ContactJoinData,name="ContactJoinData")
]