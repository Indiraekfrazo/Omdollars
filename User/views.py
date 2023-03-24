from django.shortcuts import render
from django.db import models
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import viewsets, status
from django.db.models import Q
# Create your views here.



class RoleAPIView(APIView):
    def post(self,request):
        data = request.data
        name = data.get('name')
        description = data.get('description')
        access = data.get('access')
        if data:
            if Role.objects.filter(Q(name=name)).exists():
                return Response({'Error':'User Already Exists'})
            else:
                role=Role.objects.create(name=name,description=description,access=access)

            return Response({"Message":"Data Sucessfully Added","Status": "HTTP_201_CREATED"})
        else:
            return Response({"Error":"Data Already Exists","status":"status.HTTP_400_BAD_REQUEST"})


    def get(self,request):
        id = request.query_params.get('id')
        if id:
            data=Role.objects.filter(id=id).values()
            return Response({"Message":data})
        else:
            data=Role.objects.all().values()
            return Response({"MESSAGE": "ALL DATA" , "Status": "HTTP_200_OK", 'DATA': data})
        

    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Role.objects.filter(id=id).update(name=data.get('name'),description=data.get('description'),access=data.get('access'))
            if data:
                    return Response({'message': 'Data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Id Required.'})



    def delete(self, request):
        id =self.request.query_params.get('id')
        item = Role.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response({'result':{'Status':'Data Deleted Sucessfully'}})
        else:
            return Response({'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        



class RateCardAPIView(APIView):
    def post(self,request):
        data = request.data
        work = data.get('work')
        rate = data.get('rate')
        description = data.get('description')
        if data:
            if RateCard.objects.filter(Q(work=work)).exists():
                return Response({'Error':'User Already Exists'})
            else:
                role=RateCard.objects.create(work=work,description=description,rate=rate)

            return Response({"Message":"Data Sucessfully Added","Status": "HTTP_201_CREATED"})
        else:
            return Response({"Error":"Data Already Exists","status":"status.HTTP_400_BAD_REQUEST"})


    def get(self,request):
        id = request.query_params.get('id')
        if id:
            data=RateCard.objects.filter(id=id).values()
            return Response({"Message":data})
        else:
            data=RateCard.objects.all().values()
            return Response({"MESSAGE": "ALL DATA" , "Status": "HTTP_200_OK", 'DATA': data})
        

    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = RateCard.objects.filter(id=id).update(work=data.get('work'),description=data.get('description'),rate=data.get('rate'))
            if data:
                    return Response({'message': 'Data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Id Required.'})



    def delete(self, request):
        id =self.request.query_params.get('id')
        item = RateCard.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response({'result':{'Status':'Data Deleted Sucessfully'}})
        else:
            return Response({'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)
        

class ProjectstatusAPIView(APIView):
    def post(self,request):
        data = request.data
        name = data.get('name')
        description = data.get('description')
        if data:
            if Projectstatus.objects.filter(Q(name=name)).exists():
                return Response({'Error':'User Already Exists'})
            else:
                role=Projectstatus.objects.create(name=name,description=description)

            return Response({"Message":"Data Sucessfully Added","Status": "HTTP_201_CREATED"})
        else:
            return Response({"Error":"Data Already Exists","status":"status.HTTP_400_BAD_REQUEST"})


    def get(self,request):
        id = request.query_params.get('id')
        if id:
            data=Projectstatus.objects.filter(id=id).values()
            return Response({"Message":data})
        else:
            data=Projectstatus.objects.all().values()
            return Response({"MESSAGE": "ALL DATA" , "Status": "HTTP_200_OK", 'DATA': data})
        

    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Projectstatus.objects.filter(id=id).update(name = data.get('name'),description=data.get('description'))
            if data:
                    return Response({'message': 'Data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Id Required.'})



    def delete(self, request):
        id =self.request.query_params.get('id')
        item = Projectstatus.objects.filter(id= id)
        if len(item) > 0:
            item.delete()
            return Response({'result':{'Status':'Data Deleted Sucessfully'}})
        else:
            return Response({'error':{'message':'Record not found!',
                'status_code':status.HTTP_404_NOT_FOUND,
                }},status=status.HTTP_404_NOT_FOUND)