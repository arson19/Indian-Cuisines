from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from foodmembers.custom_authentication import Custom_Auth
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Members
from .serializers import MemberSerializer

from backend.models import Foods
from backend.serializers import FoodSerializer

# Create your views here.

class MemberFunctions(APIView):
	
	
	def post(self,request,**kwargs):
		
		serializer=FoodSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

	def put(self,request,**kwargs):
		
		a=Foods.objects.get(name=self.kwargs['name'])
		serializer=FoodSerializer(a,data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

	def delete(self,request,**kwargs):
		
		try:
			a=Foods.objects.filter(food=self.request.GET.get('name'))
			a.delete()
		except Exception as e:
			return Response(status=status.HTTP_417_EXPECTATION_FAILED)
		return Response(status=status.HTTP_200_OK)
		



class AddMember(APIView):
	

	def post(self,request,**kwargs):
		a=request.data
		serializer=MemberSerializer(data=a)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	
