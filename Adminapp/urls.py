from django.urls import path
from.import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('addIndexPage',views.addIndexPage,name='addIndexPage'),
    path('tablePage',views.tablePage,name='tablePage'),
    path('getdata',views.getdata,name='getdata'),   
    path('ViewContactTable',views.ViewContactTable,name='ViewContactTable'),
    path('AdminLogin',views.AdminLogin,name='AdminLogin'),
    path('getlogin',views.getlogin,name='getlogin')

]
