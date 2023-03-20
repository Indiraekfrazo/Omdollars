from django.db.models import fields
from .models import *
from  rest_framework import serializers




class CustomUserSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        