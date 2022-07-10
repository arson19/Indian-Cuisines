from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.



class Members(AbstractBaseUser):
	username=models.CharField(max_length=100,unique=True)
	email=models.EmailField(max_length=40,unique=True)
	contrib=models.IntegerField()
	is_active=models.BooleanField(True)

	USERNAME_FIELD= 'username'
	REQUIRED_FIELDS=['email']

	objects=UserManager()

	def __str__(self):
		return self.username

	class Meta:
		db_table='members'
