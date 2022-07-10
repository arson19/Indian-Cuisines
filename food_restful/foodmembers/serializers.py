from .models import Members
from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model='Members'
		fields=['username','email','password','contrib']
