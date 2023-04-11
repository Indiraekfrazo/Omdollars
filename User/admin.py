from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Role)
class Role(admin.ModelAdmin):
    list_display = ['id','name','access','created_datetime','updated_datetime']


@admin.register(RateCard)
class RateCard(admin.ModelAdmin):
    list_display = ['id','sl_no','work','rate','created_datetime','updated_datetime']
    

@admin.register(Projectstatus)
class Projectstatus(admin.ModelAdmin):
    list_display = ['id','name','description','created_datetime','updated_datetime']