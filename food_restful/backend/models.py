from django.db import models


class Foods(models.Model):
    food = models.CharField(max_length=50, blank=True, null=True)
    ingredients = models.CharField(max_length=100, blank=True, null=True)
    diet = models.CharField(max_length=50, blank=True, null=True)
    prep_time = models.CharField(max_length=5,blank=True, null=True)
    cook_time = models.CharField(max_length=5,blank=True, null=True)
    flavour_profile = models.CharField(max_length=20, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    states = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)

    


