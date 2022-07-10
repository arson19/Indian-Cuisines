from .models import Foods
from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
	class Meta:
		model=Foods
		fields=['food','ingredients','diet','prep_time','cook_time','region','states','course','flavour_profile']