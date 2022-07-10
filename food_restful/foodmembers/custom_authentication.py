from .models import Members
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class Custom_Auth(BaseAuthentication):

	def authenticate(self,request):
		username=request.POST.post('username')

		if username is None:
			return None
		try:
			user=Members.objects.get(username=username)
		except Exception:
			raise AuthenticationFailed('No such User')
		return (user,None)
