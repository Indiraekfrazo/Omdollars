from django.db import models
from django.contrib.auth.models import User
from User.models import *
# Create your models here.

class CustomUser(models.Model):
    user = models.ForeignKey(User,null=True, on_delete= models.CASCADE)
    user_name = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email= models.EmailField(max_length=50, null=True, blank=True)
    password=models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone_number=models.CharField(max_length=50, null=True, blank=True)
    age = models .IntegerField()
    om_dollars_balance = models.CharField(max_length=200, null=True, blank=True)
    photo = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True, null=True)
    role_id = models.ForeignKey(Role,null=True, on_delete= models.CASCADE,related_name="role_on_customuser")



    def __str__(self):
        return self.user_name