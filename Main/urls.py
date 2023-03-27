from django.urls import path, include
from rest_framework import routers
from .views  import *




app_name = 'Main'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(),name='register'),
    path('login/', LoginAPIView.as_view(),name='login'),
    path('projects/', ProjectAPIView.as_view(),name='Projects'),
    path('projects/<int:pk>', ProjectAPIView.as_view(),name='Projects_details'),
]