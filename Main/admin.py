from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['id','user','user_name','first_name','last_name','email','password','address','phone_number','age','om_dollars_balance',
                    'photo','created_datetime','updated_datetime','role_id']