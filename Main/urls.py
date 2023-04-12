from django.urls import path, include
from rest_framework import routers
from .views  import *




app_name = 'Main'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(),name='register'),
    path('login/', LoginAPIView.as_view(),name='login'),
    path('forgotpassword/',ForgotPasswordAPIView.as_view(),name='ForgotPassword'),
    path('projects/', ProjectAPIView.as_view(),name='Projects'),
    path('projects/<int:pk>', ProjectAPIView.as_view(),name='Projects_details'),
    path('supervisor/', SupervisorAPIView.as_view(),name='supervisor'),
    path('supervisor/<int:pk>', SupervisorAPIView.as_view(),name='supervisor_details'),
    path('projectbid/', ProjectbidsAPIView.as_view(),name='projectbid'),
    path('projectbid/<int:pk>', ProjectbidsAPIView.as_view(),name='projectbid_details'),
    path('supervisorprojectdetail/', SupervisorProjectDetailAPIView.as_view(),name='supervisorproject'),
    path('supervisorprojectdetail/<int:pk>', SupervisorProjectDetailAPIView.as_view(),name='supervisorproject_details'),
    path('notes/', NotesAPIView.as_view(),name='notes'),
    path('notes/<int:pk>', NotesAPIView.as_view(),name='notes_details'),
    path('comment/', CommentsAPIView.as_view(),name='comment'),
    path('comment/<int:pk>', CommentsAPIView.as_view(),name='comment_details'),
    path('taskdetail/', TaskdetailAPIView.as_view(), name = 'taskdetail'),
    path('taskdetail/<int:pk>', TaskdetailAPIView.as_view(),name='taskdetail_details'),
    path('projectforstudents/', StudentProjectAPIView.as_view(), name ='projectforstudents')
    
]