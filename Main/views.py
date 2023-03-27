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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.utils import IntegrityError

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
        
def tokenFunction(user_id):
    user_obj = CustomUser.objects.get(user_id=user_id)
    user = User.objects.get(id=user_id)
    auth_token = jwt.encode(
        {'cuser_id':user_id,"username":user_obj.user_name,
        }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
    authorization = 'Bearer'+' '+str(auth_token)
    response_result = {}
    response = {}
    response_result['result'] = {
        'detail': 'Login successfull',
        'cuser_id':user_id,
        'token':authorization,
        'status': status.HTTP_200_OK
            }
    response['Authorization'] = authorization 
    response['status'] = status.HTTP_200_OK
    response['username']=user.username
    response['user_id']=user_id

    return response 



class LoginAPIView(APIView):
    def post(self,request):
        #breakpoint()
        data = request.data
        username = data.get('username')
        role = data.get('role')
        password = data.get('password')
        response ={}
        if role == 'ADMIN':
            if User.objects.filter(username=username).exists() and org_password == True:
                org_password = check_password(password, User.objects.get(username=username).password)
                cuser_obj= User.objects.get(username=username)
                user_token = tokenFunction(cuser_obj.id)
                return Response(user_token)
            else:
                return Response({"error":"User does Not exit"})
                
        if role == "SUPERVISER":
            if username is not None and password is not None:
                usr_password = check_password(password, User.objects.get(username=username).password)
                if User.objects.filter(username=username).exists():
                    user_obj = User.objects.get(username=username)
                    user_token = tokenFunction(user_obj.id)
                return Response(user_token)
            else:
                return Response({"error":"Invalid Credentails"},status=status.HTTP_404_NOT_FOUND )
                    
        if role == 'STUDENT':
            if User.objects.filter(username=username).exists() and org_password == True:
                org_password = check_password(password, User.objects.get(username=username).password)
                cuser_obj= User.objects.get(username=username)
                        #user_id =CustomUser.objects.get(Q(phone_number=phone_number))
                user_token = tokenFunction(cuser_obj.id)
                return Response(user_token)
            else:
                return Response({"error":"User does Not exit"})
                
        # else:
        #     header_response = {}
        #     response['error'] = {'error': {
        #                 'detail': 'Invalid Email / Password', 'status': status.HTTP_401_UNAUTHORIZED}}   #incorrect username and password
        #     return Response(response['error'],headers=header_response,status= status.HTTP_401_UNAUTHORIZED)
        else:
            response['error'] = {'error': {
                'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
            return Response({'message': 'User account does  Not exit'},response['error'], status= status.HTTP_401_UNAUTHORIZED)
        




class ProjectAPIView(APIView):
    def post(self,request):
        data = request.data
        project_name = data.get('project_name')
        estimated_hours = data.get('estimated_hours')
        estimation_completion_time = data.get('estimation_completion_time')
        description_of_work = data.get('description_of_work')
        outcome_required = data.get('outcome_required')
        estimated_value_rate = data.get('estimated_value_rate')
        terms_and_conditions = data.get('terms_and_conditions')
        is_accepted_tnc = data.get('is_accepted_tnc')
        project_status= data.get('project_status_id')
        user_ref= data.get('user_ref_id')
        selected_page_no =1 
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)
        try:
            if Projects.objects.filter(Q(project_name=project_name)).exists():
                return Response({'Error':'Project_name Already Exists'})
            else:

                Projects.objects.create(project_name=project_name,
                                        estimated_hours = estimated_hours,
                                        estimation_completion_time = estimation_completion_time,
                                        description_of_work=description_of_work,
                                        outcome_required = outcome_required,
                                        estimated_value_rate=estimated_value_rate,
                                        terms_and_conditions = terms_and_conditions,
                                        is_accepted_tnc = is_accepted_tnc,
                                        project_status_id = project_status,
                                        user_ref_id= user_ref,
                                        )
                project = Projects.objects.all().values()
                paginator = Paginator(project,10)
            try:
                page_obj = paginator.get_page(selected_page_no)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except:
                page_obj = paginator.page(paginator.num_pages)
            return Response({'result':{'status':'Data created sucdessfully','data':list(page_obj)}})
        except IntegrityError as e:
            error_message = e.args
            return Response({
            'error':{'message':'DB error!',
            'detail':error_message,
            'status_code':status.HTTP_400_BAD_REQUEST,
            }},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        id = request.query_params.get('id')
        if id:
            try:
                all_data = Projects.objects.filter(id=id).values()
                return Response({'result':{'status':'GET by id','data':all_data}})
            except Projects.DoesNotExist:
                return Response({
                'error':{'message':'Id does not exists!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            all_data = Projects.objects.all().values()
            return Response({'result':{'status':'All data','data':all_data}})
        

    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Projects.objects.filter(id=id).update(project_name = data.get("project_name"),
                                        estimated_hours = data.get("estimated_hours"),
                                        estimation_completion_time = data.get("estimation_completion_time"),
                                        description_of_work=data.get("description_of_work"),
                                        outcome_required = data.get("outcome_required"),
                                        estimated_value_rate=data.get("estimated_value_rate"),
                                        terms_and_conditions = data.get("terms_and_conditions"),
                                        is_accepted_tnc = data.get("is_accepted_tnc"),
                                        project_status = data.get("project_status"),
                                        user_ref = data.get("user"),
                                        )
            if data:
                    return Response({'message': 'Data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Id Required.'})



    def delete(self, request):
        id =self.request.query_params.get('id')
        item = Projects.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response({'result':{'Status':'Data Deleted Sucessfully'}})
        else:
            return Response({'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)

    