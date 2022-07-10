from django.urls import path
from .views import List_food,List_by_param
urlpatterns=[
				#path('login', view),
				path('food/', List_food.as_view()),
				path('food/<str:param>', List_by_param.as_view()),
				
				


			

			]