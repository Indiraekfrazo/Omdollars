from django.urls import path, include
from rest_framework import routers
from .views  import *




app_name = 'User'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('role/', RoleAPIView.as_view(),name='ROLE'),
    path('role/<int:pk>', RoleAPIView.as_view(),name='ROLE_Detail'),

]