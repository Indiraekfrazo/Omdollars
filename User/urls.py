from django.urls import path, include
from rest_framework import routers
from .views  import *




app_name = 'User'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('role/', RoleAPIView.as_view(),name='ROLE'),
    path('role/<int:pk>', RoleAPIView.as_view(),name='ROLE_Detail'),
    path('ratecard/', RateCardAPIView.as_view(),name='RateCard'),
    path('ratecard/<int:pk>', RateCardAPIView.as_view(),name='RateCard_deatil'),
    path('projectstatus/', ProjectstatusAPIView.as_view(),name='Projectstatus'),
    path('projectstatus/<int:pk>', ProjectstatusAPIView.as_view(),name='Projectstatus'),
]