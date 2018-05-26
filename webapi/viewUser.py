from django.db.models import Q
from django.contrib.auth import get_user_model
from .serializerUser import UserSerializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.filters import(
        SearchFilter,
        OrderingFilter,
	)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,

	)

User = get_user_model()

from .serializerUser import (
   # UserCreateSerializer,
    UserSerializers,
    UserLoginSerializer
	)




class UserCreateAPIView(generics.CreateAPIView):
	lookup_field = 'matricule'
	serializer_class = UserSerializers
	queryset     = User.objects.all()  

def get_queryset(self):
    return User.objects.all()

def perform_create(self, serializer):
	serializer.save(user=self.request.user)        

class UserLoginAPTView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    


    def post(self, request, *args , **kwargs):
    	data = request.data
    	serializer = UserLoginSerializer(data=data)
    	if serializer.is_valid(raise_exception=True):
    		new_data = serializer.data
    		return Response(new_data,status=HTTP_200_OK)
    	return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
class UserAPIViewList(generics.ListAPIView):
	lookup_field = 'matricule'
	serializer_class = UserSerializers
	queryset     = User.objects.all()  

def get_queryset(self):
    return User.objects.all()

def perform_create(self, serializer):
	serializer.save(user=self.request.user)

class UserRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'matricule'
	serializer_class = UserSerializers
	queryset     = User.objects.all()  

def get_queryset(self):
    return User.objects.all()