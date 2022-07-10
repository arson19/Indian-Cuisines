from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
	def create_user(self,email,contrib,password=None):
		if not email or not username:
			 raise ValueError('Must provide username and email')
		user=self.model(email=normalize_email(email),contrib=contrib)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self,email,contrib,password=None):
		user=self.model(email=normalize_email(email),contrib=contrib)
		user.set_password(password)
		user.is_admin=True
		user.save()
		return user