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
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.utils import IntegrityError
#from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth
from rest_framework.authtoken.views import ObtainAuthToken
from django.core.mail import message, send_mail, EmailMessage
# Create your views here.

class RegisterAPIView(APIView):
    def post(self,request):
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
        # user_role = Role.objects.get(id=role_id)
        # username =user_role.name
        response_result= {}
        
        if CustomUser.objects.filter(Q(user_name=user_name)).exists():
            return Response({'error':{'detail':'User already exists'}}, status=status.HTTP_406_NOT_ACCEPTABLE) 
        elif User.objects.filter(Q(username=user_name)).exists():
            return Response({'error':{'detail':'Username already exists'}}, status=status.HTTP_406_NOT_ACCEPTABLE) 
        else:
            # user role 2
            # admin role 1
                create_user = User.objects.create(username=user_name,email=email,password=make_password(password))
                if role_id is not None:
                    store_otp = CustomUser.objects.create(
                                user_id = create_user.id,
                                user_name = user_name,
                                first_name = first_name,
                                email = email,
                                password = password,
                                address = address,
                                phone_number = phone_number,
                                age = age,
                                om_dollars_balance = om_dollars_balance,
                                profile_image_path = profile_image_path,
                                role_id_id= role_id,
                          )                
                else:    
                    store_otp = CustomUser.objects.create(user_id =create_user.id, user_name = user_name,
                                first_name = first_name,
                                email = email,
                                password = password,
                                address = address,
                                phone_number = phone_number,
                                age = age,
                                om_dollars_balance = om_dollars_balance,
                                profile_image_path = profile_image_path,
                                role_id=1
                                )
                auth_token = jwt.encode(
                                    {'user_name':user_name,

                                    }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                print(auth_token,'this is auth_token')
                authorization = 'Bearer'+' '+str(auth_token)
                response_result = {}
                response = {}
                response_result['result'] = {
                            'result': {'data': 'Register successful',
                            'token':authorization,
                            'user_id':store_otp.id,
                            'username':user_name,
                            }}
                response['Authorization'] = authorization
                response['status'] = status.HTTP_200_OK
                return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)
        
# class RegisterAPIView(APIView):
#     def post(self,request):
#         #breakpoint()
#         data = request.data
#         user_name = data['user_name']  
#         first_name = data['first_name']  
#         last_name = data['last_name']  
#         phone_number = data['phone_number']
#         email = data['email']
#         password = data['password']
#         address = data['address']
#         age = data['age']
#         om_dollars_balance = data['om_dollars_balance']
#         profile_image_path = data['profile_image_path']
#         role_id = data['role_id']
#         user_role = Role.objects.get(id=role_id)
#         username =user_role.name
#         response_result= {}
#         response_result['result'] = {}
#         if data:
#             if User.objects.filter(Q(username=user_name)|Q(email=email)).exists():
#                 return Response({'error':'User Already Exists'})
#             else:
#                 create_user = User.objects.create_user(username=user_name,first_name=first_name,email=email,password=password)
#                 user_create = CustomUser.objects.create(
#                                 user_name = user_name,
#                                 first_name = first_name,
#                                 email = email,
#                                 password = password,
#                                 address = address,
#                                 phone_number = phone_number,
#                                 age = age,
#                                 om_dollars_balance = om_dollars_balance,
#                                 profile_image_path = profile_image_path,
#                                 role_id_id= role_id
#                                 )

#             auth_token = jwt.encode(
#                                     {'username':user_name,'email':email,'password':password
                                     
#                                     }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
#             print(auth_token,'this is auth_token')
#             authorization = 'Bearer'+' '+str(auth_token)
#                 #
#             response_result = {}
#             response = {}
#             response_result['result'] = {
#                         'result': {'data': 'Register successful',
#                         'token':authorization,
#                         'first_name':first_name,
#                         'username':user_name,
#                         "email":email,
#                             }}
#             response['Authorization'] = authorization
#             response['status'] = status.HTTP_200_OK
#             return Response(response_result['result'], headers=response,status= status.HTTP_200_OK) 
        
# def tokenFunction(user_id):
#     breakpoint()
#     user_obj = CustomUser.objects.get(user_id=user_id)
#     user = User.objects.get(id=user_id)
#     auth_token = jwt.encode(
#         {'cuser_id':user_id,"username":user_obj.user_name,
#         }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
#     authorization = 'Bearer'+' '+str(auth_token)
#     response_result = {}
#     response = {}
#     response_result['result'] = {
#         'detail': 'Login successfull',
#         'cuser_id':user_id,
#         'token':authorization,
#         'status': status.HTTP_200_OK
#             }
#     response['Authorization'] = authorization 
#     response['status'] = status.HTTP_200_OK
#     response['username']=user_obj.user_name
#     response['user_id']=user_id
#     return response 



class LoginAPIView(APIView):
    def post(self,request):
        #breakpoint()
        data = request.data
        username = data.get('user_name')
        role = data.get('role')
        password = data.get('password')
        response ={}
        data_dict = {}
        if role == 'ADMIN':
            if CustomUser.objects.filter(user_name=username,password=password).exists():
                org_password =CustomUser.objects.get(user_name=username).password
                cuser_obj= CustomUser.objects.get(user_name=username)
                auth_token = jwt.encode(
                    {'cuser_id':cuser_obj.id,"user_name":username ,
                    }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                authorization = 'Bearer'+' '+str(auth_token)
                response_result = {}
                response = {}
                response_result['result'] = {
                        'detail': 'Login successfull',
                        'cuser_id':cuser_obj.id,
                        'user_name':username,
                        'token':authorization,
                        'status': status.HTTP_200_OK
                        }
                return Response(response_result, headers=response,status= status.HTTP_200_OK)
            else:
                return Response({"error":"User does Not exit"})
                
        if role == "SUPERVISOR":
            if username is not None and password is not None:
                usr_password = check_password(password, CustomUser.objects.get(user_name=username).password)
                if CustomUser.objects.filter(user_name=username).exists():
                    user_obj = CustomUser.objects.get(user_name=username)
                    auth_token = jwt.encode(
                        {'cuser_id':user_obj.id,"user_name":username ,
                        }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                    authorization = 'Bearer'+' '+str(auth_token)
                    response_result = {}
                    response = {}
                    response_result['result'] = {
                            'detail': 'Login successfull',
                            'cuser_id':user_obj.id,
                            'user_name':username,
                            'token':authorization,
                            'status': status.HTTP_200_OK
                        }
                    return Response(response_result, headers=response,status= status.HTTP_200_OK)
                else:
                    return Response({"error":"Invalid Credentails"},status=status.HTTP_404_NOT_FOUND )
                    
        if role == 'STUDENT':
            if CustomUser.objects.filter(user_name=username,password=password).exists():
                org_password =CustomUser.objects.get(user_name=username).password
                cuser_obj= CustomUser.objects.get(user_name=username)
                    #user_id =CustomUser.objects.get(Q(phone_number=phone_number))
                auth_token = jwt.encode(
                        {'cuser_id':cuser_obj.id,"user_name":username ,
                        }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                authorization = 'Bearer'+' '+str(auth_token)
                response_result = {}
                response = {}
                response_result['result'] = {
                        'detail': 'Login successfull',
                        'cuser_id':cuser_obj.id,
                        'user_name':username,
                        'token':authorization,
                        'status': status.HTTP_200_OK
                        }  
                return Response(response_result, headers=response,status= status.HTTP_200_OK) 
        else:
            header_response = {}
            response['error'] = {'error': {
                        'detail': 'Invalid Email / Password', 'status': status.HTTP_401_UNAUTHORIZED}}   #incorrect username and password
            return Response(response['error'],headers=header_response,status= status.HTTP_401_UNAUTHORIZED)
        
        response['error'] = {'error': {
        'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
        return Response({'message': 'User account does  Not exit'},response['error'], status= status.HTTP_401_UNAUTHORIZED)

#This loginapiview for  username and password 
# class LoginAPIView(APIView):
#     def post(self,request):
#         data = request.data
#         username = data.get('user_name')
#         role = data.get('role')
#         password = data.get('password')
#         response ={}
#         if CustomUser.objects.filter(Q(user_name=username) & Q(password =password)).exists():
#             cuser = CustomUser.objects.get(Q(user_name=username))
#             data_dict = {}
#             if cuser:
#                 auth_token = jwt.encode(
#                     {'cuser_id':cuser.id,"user_name":username,
#                     }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
#                 authorization = 'Bearer'+' '+str(auth_token)
#                 response_result = {}
#                 response = {}
#                 response_result['result'] = {
#                     'detail': 'Login successfully',
#                     'cuser_id':cuser.id,
#                     'token':authorization,
#                     'status': status.HTTP_200_OK
#                     }
#                 response['Authorization'] = authorization
#                 response['status'] = status.HTTP_200_OK
#                 return Response(response_result['result'], headers=response,status= status.HTTP_200_OK)
#             else:
#                 header_response = {}
#                 response['error'] = {'error': {
#                     'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
#                 return Response(response['error'], headers=header_response,status= status.HTTP_401_UNAUTHORIZED)
#         else:
#             response['error'] = {'error': {
#                     'detail': 'Invalid Username / Password', 'status': status.HTTP_401_UNAUTHORIZED}}
#             return Response(response['error'], status= status.HTTP_401_UNAUTHORIZED)


class ForgotPasswordAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('user_name')
        password = data.get('password')
        user_check = CustomUser.objects.filter(user_name= username)
        if user_check:
            user_data = CustomUser.objects.get(user_name= username)
            user_data.set_password(password)
            user_data.save()
            message= 'Hello!\nYour password has been updated sucessfully. '
            subject= 'Password Updated Sucessfully '
            email = EmailMessage(subject, message, to=[user_data.email])
            email.send()
            return Response({'result':{'message': 'Password Updated Sucessfully'}})
        else:
            return Response({'error':{'message': 'Please Enter Valid username'}})


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

class SupervisorAPIView(APIView):
    def post(self,request):
        data = request.data
        name = data.get('name')
        status= data.get('status')
        user_id= data.get('user_id')
        selected_page_no =1 
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)
        try:
            if Supervisor.objects.filter(Q(name=name)).exists():
                return Response({'Error':'Project_name Already Exists'})
            else:

                Supervisor.objects.create(name=name,
                                        status = status,
                                        user_id_id= user_id,
                                        )
                project = Supervisor.objects.all().values()
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
                all_data = Supervisor.objects.filter(id=id).values()
                return Response({'result':{'status':'GET by id','data':all_data}})
            except Supervisor.DoesNotExist:
                return Response({
                'error':{'message':'Id does not exists!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            all_data = Supervisor.objects.all().values()
            return Response({'result':{'status':'All data','data':all_data}})
        

    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Supervisor.objects.filter(id=id).update(name = data.get("name"),
                                        status = data.get("status"),
                                        user_id = data.get("user_id"),
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
        item = Supervisor.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response({'result':{'Status':'Data Deleted Sucessfully'}})
        else:
            return Response({'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        

    
class ProjectbidsAPIView(APIView):
    def post(self,request):
        data = request.data
        description = data.get('description')
        user_id= data.get('user_id')
        project_id= data.get('project_id')
        created_datetime =data.get('created_datetime')
        updated_datetime= data.get('updated_datetime')
        selected_page_no =1 
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)
        try:
            if data:

                Projectbids.objects.create(description=description,
                                        user_id_id = user_id,
                                        project_id_id= project_id,
                                        created_datetime = created_datetime,
                                        updated_datetime= updated_datetime
                                        )
                project = Projectbids.objects.all().values()
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
                all_data = Projectbids.objects.filter(id=id).values()
                return Response({'result':{'status':'GET by id','data':all_data}})
            except Projectbids.DoesNotExist:
                return Response({
                'error':{'message':'Id does not exists!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            all_data = Projectbids.objects.all().values()
            return Response({'result':{'status':'All data','data':all_data}})
        

    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Projectbids.objects.filter(id=id).update(description = data.get('description'),
                                                                user_id= data.get('user_id'),
                                                                project_id= data.get('project_id')
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
        item = Projectbids.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response({'result':{'Status':'Data Deleted Sucessfully'}})
        else:
            return Response({'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        

    
class SupervisorProjectDetailAPIView(APIView):
    def post(self,request):
        data = request.data
        name  = data.get('name')
        user_id= data.get('user_id')
        status_id = data.get('status_id')
        project_id= data.get('project_id')
        created_datetime =data.get('created_datetime')
        updated_datetime= data.get('updated_datetime')
        selected_page_no =1 
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)
        try:
            if data:
                SupervisorProjectDetail.objects.create(name=name,
                                        user_id_id = user_id,
                                        status_id_id =status_id,
                                        project_id_id= project_id,
                                        created_datetime = created_datetime,
                                        updated_datetime = updated_datetime
                                        )
                project = SupervisorProjectDetail.objects.all().values()
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
                all_data = SupervisorProjectDetail.objects.filter(id=id).values()
                return Response({'result':{'status':'GET by id','data':all_data}})
            except SupervisorProjectDetail.DoesNotExist:
                return Response({
                'error':{'message':'Id does not exists!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            all_data = SupervisorProjectDetail.objects.all().values()
            return Response({'result':{'status':'All data','data':all_data}})
        

    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = SupervisorProjectDetail.objects.filter(id=id).update(name = data.get('name'),
                                                        user_id= data.get('user_id'),
                                                        status_id = data.get('status_id'),
                                                        project_id= data.get('project_id'),
                    
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
        item = SupervisorProjectDetail.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response({'result':{'Status':'Data Deleted Sucessfully'}})
        else:
            return Response({'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        

class NotesAPIView(APIView):
    def post(self,request):
        data = request.data
        notes  = data.get('notes')
        user_id= data.get('user_id')
        project_id= data.get('project_id')
        created_datetime =data.get('created_datetime')
        updated_datetime= data.get('updated_datetime')
        selected_page_no =1 
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)
        try:
            if data:
                Notes.objects.create(notes=notes,
                                        user_id_id = user_id,
                                        project_id_id= project_id,
                                        created_datetime = created_datetime,
                                        updated_datetime = updated_datetime
                                        )
                project = Notes.objects.all().values()
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
                all_data = Notes.objects.filter(id=id).values()
                return Response({'result':{'status':'GET by id','data':all_data}})
            except Notes.DoesNotExist:
                return Response({
                'error':{'message':'Id does not exists!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            all_data = Notes.objects.all().values()
            return Response({'result':{'status':'All data','data':all_data}})
        

    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Notes.objects.filter(id=id).update(notes  = data.get('notes'),
                                                    user_id= data.get('user_id'),
                                                    project_id= data.get('project_id'),
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
        item = Notes.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response({'result':{'Status':'Data Deleted Sucessfully'}})
        else:
            return Response({'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        

class CommentsAPIView(APIView):
    def post(self,request):
        data = request.data
        comment  = data.get('comment')
        user_id= data.get('user_id')
        project_id= data.get('project_id')
        created_datetime =data.get('created_datetime')
        updated_datetime= data.get('updated_datetime')
        selected_page_no =1 
        page_number = request.GET.get('page')
        if page_number:
            selected_page_no = int(page_number)
        try:
            if data:
                Comments.objects.create(comment=comment,
                                        user_id_id = user_id,
                                        project_id_id= project_id,
                                        created_datetime = created_datetime,
                                        updated_datetime = updated_datetime
                                        )
                project = Comments.objects.all().values()
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
                all_data = Comments.objects.filter(id=id).values()
                return Response({'result':{'status':'GET by id','data':all_data}})
            except Comments.DoesNotExist:
                return Response({
                'error':{'message':'Id does not exists!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        else:
            all_data = Comments.objects.all().values()
            return Response({'result':{'status':'All data','data':all_data}})
        

    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Comments.objects.filter(id=id).update(comment  = data.get('comment'),
                                                    user_id= data.get('user_id'),
                                                    project_id= data.get('project_id'),
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
        item = Comments.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response({'result':{'Status':'Data Deleted Sucessfully'}})
        else:
            return Response({'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        