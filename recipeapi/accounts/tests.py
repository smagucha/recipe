# from django.test import TestCase
# #from accounts.models import User
# from django.contrib.auth import get_user_model
# class Test_User(TestCase):
# 	def test_User_superuser(self):

# 		d=get_user_model()
# 		super_user= d.objects.create_superuser(
# 			"smagucha@gmail.com","userJohnDoe", "secretpassword")
# 		self.assertEqual(super_user.email, 'smagucha@gmail.com')
# 		self.assertEqual(super_user.username, 'userJohnDoe')
# 		self.assertTrue(super_user.is_admin)
# 		self.assertTrue(super_user.is_superuser)
# 		self.assertTrue(super_user.is_staff)
# 		self.assertTrue(super_user.is_active)
# 		self.assertEqual(str(super_user.email), 'smagucha@gmail.com')
# 		with self.assertRaises(ValueError):
# 			super_user= User.objects.create('smagucha@gmail.com',"userJohnDoe", "secretpassword", is_superuser=False)

# 	def test_new_user(self):
# 		d=get_user_model()
# 		user= d.objects.create_user('smacha@gmail.com',"userDoe", "password")
# 		self.assertEqual(user.email, 'smacha@gmail.com')
# 		self.assertFalse(user.is_admin)
# 		self.assertFalse(user.is_staff)
# 		self.assertTrue(user.is_active)
# 		self.assertFalse(user.is_superuser)
		


		

