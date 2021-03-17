from django.test import TestCase
from accounts.models import User

class Test_User(TestCase):
	def test_User(self):
		user= User.objects.create(email='smagucha@gmail.com', username="userJohnDoe", password="secretpassword", )
		
		self.assertEqual(str(email), 'smagucha@gmail.com')

