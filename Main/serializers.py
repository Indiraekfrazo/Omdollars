from django.db.models import fields
from .models import *
from  rest_framework import serializers




class CustomUserSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class ProjecSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Projects
        fields = '__all__'

class ProjectbidSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Projectbids
        fields = '__all__'

class SupervisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supervisor
        fields = '__all__'


class NotesSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = '__all__'

class CommentsSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'