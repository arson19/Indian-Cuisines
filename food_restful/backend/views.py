from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Foods
from .serializers import FoodSerializer
# Create your views here.



class List_food(APIView):
	
	def get(self,*args,**kwargs):
		a=Foods.objects.all()
		
		serializer=FoodSerializer(a,many=True)
		return Response(serializer.data)
	

class List_by_param(APIView):
	def get(self,*args,**kwargs):
		if kwargs['param']=='veg':
			a=Foods.objects.filter(diet='vegetarian')
		elif kwargs['param']=='nonveg':
		 	a=Foods.objects.filter(diet='non vegetarian')
		else:
			a=Foods.objects.filter(states=self.kwargs['param'])
		serializer=FoodSerializer(a,many=True)
		return Response(serializer.data)
'''
class AddMember(APIView):
	def post(self,request,**kwargs):
		a=request.data
		serializer=MemberSerializer(data=a)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)
	def get(self,*args,**kwargs):
		a=Members.objects.all()
		serializer=MemberSerializer(a,many=True)
		return Response(serializer.data)
		
class MemberRights(APIView):
	authentication_classes=[SessionAuthentication,BasicAuthentication]
	permissions=[IsAuthenticated]
	def post(self,request,**kwargs):
		serializer=FoodSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)
	def put(self,request,pk):
		serializer=FoodSerializer(data=request.data)
'''
