from .models import Members
from django.urls import path
from .views import MemberFunctions,AddMember
urlpatterns=[
				path('member',MemberFunctions.as_view()),
				path('member/<str:name>', MemberFunctions.as_view()),
				path('add', AddMember.as_view()),
			]