from django.contrib import admin
from .models import *



# Register your models here.
@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['id','user','user_name','first_name','last_name','email','password','address','phone_number','age','om_dollars_balance',
                    'profile_image_path','created_datetime','updated_datetime','role_id']
    

@admin.register(Projects)
class Projects(admin.ModelAdmin):
    list_display = [ "id","project_name","estimated_hours","estimation_completion_time","description","outcome_required","Skillset",
                    "estimated_value_rate","terms_and_conditions","is_accepted_tnc","project_status","user_ref",
                    "created_datetime","updated_datetime"]
    
@admin.register(Supervisor)
class Supervisor(admin.ModelAdmin):
    list_display = [ "id","name","email","mobile_number","status","user_id","created_datetime","updated_datetime"]


@admin.register(Projectbids)
class Projectbids(admin.ModelAdmin):
    list_display = [ "id","description","user_id","project_id","created_datetime","updated_datetime"]


@admin.register(SupervisorProjectDetail)
class SupervisorProjectDetail(admin.ModelAdmin):
    list_display = [ "id","name","user_id","project_id","status_id","created_datetime","updated_datetime"]


@admin.register(Notes)
class Notes(admin.ModelAdmin):
    list_display = [ "id","notes","user_id","project_id","created_datetime","updated_datetime"]

@admin.register(Comments)
class Comments(admin.ModelAdmin):
    list_display = [ "id","comment","user_id","project_id","created_datetime","updated_datetime"]

@admin.register(Taskdetail)
class Taskdetail(admin.ModelAdmin):
    list_display = [ "id","project_name","description","start_time","end_time","student_notes","student_comments","status",
                    "reason","superviser"]
    
@admin.register(StudentProjects)
class StudentProjects(admin.ModelAdmin):
    list_display = [ "id","student","project_name"]

@admin.register(Reward)
class Reward(admin.ModelAdmin):
    list_display = [ "id","s_no","description","project","allocation_amount",'withdraw_amount','closing_balance','deposit_amount']