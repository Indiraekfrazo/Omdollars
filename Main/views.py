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
from django.db.models import Q
# Create your views here.


