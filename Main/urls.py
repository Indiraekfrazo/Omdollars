from django.urls import path, include
from rest_framework import routers
from .views  import *




app_name = 'Main'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(),name='register'),

]