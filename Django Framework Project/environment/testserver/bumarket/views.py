#-*- coding: utf-8 -*- 
# 한글을 사용하면 위에 꼭 써야함
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
import json

from django.db import models
from .models import UserModel, ProductModel, SaleModel, LikeModel, SaleModel, ImageModel, UserImageModel, ProImageModel # Model import
from .serializers import UserSerializer, ProductSerializer, LikeSerializer, SaleSerializer, ImageSerializer, UserImageSerializer, ProImageSerializer # Serializer import
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate #20191002
from django.http import HttpResponse #20191004
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserJoinForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers
from rest_framework import status

from django.contrib.auth.models import User
from rest_framework import generics
import logging
logger = logging.getLogger('testlog')

####################################################################

class UserList(generics.ListCreateAPIView):
    userqueryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        userqueryset = self.get_queryset()
        userserializer = UserSerializer(userqueryset, many=True)
        return Response(userserializer.data)

####################################################################

class ProductList(generics.ListCreateAPIView):
    productqueryset = ProductModel.objects.all()
    serializer_class = ProductModel

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        productqueryset = self.get_queryset()
        productserializer = ProductSerializer(productqueryset, many=True)
        return Response(productserializer.data)
        
    #def book(self, request):
    #    productqueryset = ProductModel.objects.all()
    #    productqueryset = productqueryset.filter(ProductCategory="도서")
    #    productserializer = ProductSerializer(productqueryset, many=True)
    #    return Response(productserializer.data)

####################################################################
