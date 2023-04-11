from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=200,null=True, blank =True)
    access = models.CharField(max_length=200, null =True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class RateCard(models.Model):
    sl_no = models.CharField(max_length=200,null =True, blank=True)
    work = models.CharField(max_length=200, null =True, blank=True)
    rate = models.CharField(max_length=200, null =True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True, null=True)



class Projectstatus(models.Model):
    name = models.CharField(max_length=200, null =True, blank=True)
    description = models.CharField(max_length=200, null =True, blank=True)
    created_datetime = models.CharField(max_length=200, null =True, blank=True)
    updated_datetime = models.CharField(max_length=200, null =True, blank=True)


    def __str__(self):
        return self.name