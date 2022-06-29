from django.contrib import admin

from Userapp.models import  ContactForJoinDb, Contactdb, RegisterDb

# Register your models here.
admin.site.register(Contactdb)
admin.site.register(RegisterDb)
admin.site.register(ContactForJoinDb)