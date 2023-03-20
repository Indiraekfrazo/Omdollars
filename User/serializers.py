from django.db.models import fields
from .models import *
from  rest_framework import serializers

#Create your serializers here

class RoleSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = '__all__'



class RateCardSerilizer(serializers.ModelSerializer):

    class Meta:
        model = RateCard
        fields = '__all__'



class ProjectstatusSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Projectstatus
        fields = '__all__'
