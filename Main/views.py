from django.shortcuts import render
from django.db import models
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from .models import *
from rest_framework import viewsets, status
from rest_framework import serializers
import jwt
import re
import random
import base64
from mimetypes import guess_type, guess_extension
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

class RegisterAPIView(APIView):
    def post(self,request):
        #breakpoint()
        data = request.data
        user_name = data['user_name']  
        first_name = data['first_name']  
        last_name = data['last_name']  
        phone_number = data['phone_number']
        email = data['email']
        password = data['password']
        address = data['address']
        age = data['age']
        om_dollars_balance = data['om_dollars_balance']
        profile_image_path = data['profile_image_path']
        role_id = data['role_id']
        user_role = Role.objects.get(id=role_id)
        username =user_role.name
        response_result= {}
        response_result['result'] = {}
        if data:
            if User.objects.filter(Q(username=user_name)|Q(email=email)).exists():
                return Response({'error':'User Already Exists'})
            else:
                create_user = User.objects.create_user(username=user_name,first_name=first_name,email=email,password=password)
                user_create = CustomUser.objects.create(
                                user_name = user_name,
                                first_name = first_name,
                                email = email,
                                password = password,
                                address = address,
                                phone_number = phone_number,
                                age = age,
                                om_dollars_balance = om_dollars_balance,
                                profile_image_path = profile_image_path,
                                role_id_id= role_id
                                )

            auth_token = jwt.encode(
                                    {'username':user_name,'email':email,'password':password
                                     
                                    }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
            print(auth_token,'this is auth_token')
            authorization = 'Bearer'+' '+str(auth_token)
                #
            response_result = {}
            response = {}
            response_result['result'] = {
                        'result': {'data': 'Register successful',
                        'token':authorization,
                        'first_name':first_name,
                        'username':user_name,
                        "email":email,
                            }}
            response['Authorization'] = authorization
            response['status'] = status.HTTP_200_OK
            return Response(response_result['result'], headers=response,status= status.HTTP_200_OK) 