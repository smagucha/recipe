from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

	def create_user(self, email, username,  password=None):

		if not email:
			raise ValueError('please enter a valid email')
		if not username:
			raise ValueError('please enter a valid username')

		user = self.model(
			email=self.normalize_email(email),
			username= username,
		
			
			)
		user.set_password(password)
		user.save(using= self._db)
		return user

	def create_superuser(self, email, username, password=None):
		user= self.create_user(
			email= self.normalize_email(email),
			username= username,
			password= password,
			
			)
		user.is_admin= True
		user.is_staff= True
		user.is_superuser=True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email= models.EmailField(unique=True)
	username = models.CharField(max_length = 30, unique= True)
	date_joined = models.DateTimeField(auto_now_add=True)
	last_login=models.DateTimeField(auto_now=True)
	is_admin=models.BooleanField(default= False)
	is_active= models.BooleanField(default= True)
	is_staff=models.BooleanField(default= False)
	is_superuser = models.BooleanField(default= False)


	USERNAME_FIELD= 'email'
	REQUIRED_FIELD=['username']

	objects = UserManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True























