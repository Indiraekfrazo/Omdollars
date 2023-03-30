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
    profile_image_path= models.CharField(max_length=100, null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True, null=True)
    role_id = models.ForeignKey(Role,null=True, on_delete= models.CASCADE,related_name="role_on_customuser")



    def __str__(self):
        return self.user_name
    
class Projects(models.Model):
    project_name = models.CharField(max_length=50, null=True, blank=True)
    estimated_hours = models.CharField(max_length=50, null=True, blank=True)
    estimation_completion_time = models.CharField(max_length=50, null=True, blank=True)
    description_of_work = models.CharField(max_length=50, null=True, blank=True)
    outcome_required = models.CharField(max_length=50, null=True, blank=True)
    estimated_value_rate = models.CharField(max_length=50, null=True, blank=True)
    terms_and_conditions = models.CharField(max_length=50, null=True, blank=True)
    is_accepted_tnc = models.BooleanField()
    project_status = models.ForeignKey(Projectstatus,null=True, on_delete= models.CASCADE,related_name="status_on_projects")
    user_ref = models.ForeignKey(CustomUser,null=True, on_delete= models.CASCADE,related_name="user_on_projects")
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True, null=True)


class Supervisor(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True, null=True)
    user_id = models.ForeignKey(CustomUser,null=True, on_delete= models.CASCADE)

class Projectbids(models.Model):
    description = models.CharField(max_length=50, null=True, blank=True)
    user_id = models.ForeignKey(CustomUser,null=True, on_delete= models.CASCADE,related_name="user_on_projectbids")
    project_id = models.ForeignKey(Projects,null=True, on_delete= models.CASCADE,related_name="projects_on_projectbids")
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True, null=True)


class SupervisorProjectDetail(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    project_id = models.ForeignKey(Projects,null=True, on_delete= models.CASCADE,related_name="projects_on_superviserdetail")
    status_id = models.ForeignKey(Projectstatus,null=True, on_delete= models.CASCADE,related_name="status_on_superviserdetail")                    
    user_id = models.ForeignKey(CustomUser,null=True, on_delete= models.CASCADE,related_name="user_on_superviserdetail")
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True, null=True)


class Notes(models.Model):
    notes = models.CharField(max_length=50, null=True, blank=True)
    user_id = models.ForeignKey(CustomUser,null=True, on_delete= models.CASCADE,related_name="user_on_notes")
    project_id = models.ForeignKey(Projects,null=True, on_delete= models.CASCADE,related_name="projects_on_notes")
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True, null=True)


class Comments(models.Model):
    comment = models.CharField(max_length=50, null=True, blank=True)
    user_id = models.ForeignKey(CustomUser,null=True, on_delete= models.CASCADE,related_name="user_on_commentss")
    project_id = models.ForeignKey(Projects,null=True, on_delete= models.CASCADE,related_name="projects_on_comments")
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True, null=True)