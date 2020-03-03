from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
 

class UserManager(BaseUserManager):
	def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True, is_student=False, is_teacher=False):
		if not email:
			raise ValueError("Users must have an email address")
		if not password:
			raise ValueError("user must have a password")

		user_obj =self.model(
			email = self.normalize_email(email)
			)
		user_obj,set_password(password)
		user_obj.staff = is_staff
		user_obj.is_admin = is_admin
		user_obj.active=is_active
		user_obj.student=is_student
		user_obj.teacher=is_teacher
		user_obj.save(using=self._db)
		return user_obj
	def create_staffuser(self,email, password=None):
		user = self.create_user(
			email,password=password,is_staff=True)
		return user 

	def create_superuser(self,email, password=None):
		user = self.create_user(
			email,
			password=password,
			is_staff=True,
			is_admin=True)
		return user 

	def create_student(self,email, password=None):
		user = self.create_user(
			email,
			password=password,
			is_student=True)
		return user 

	def create_teacher(self,email, password=None):
		user = self.create_user(
			email,
			password=password,
			is_teacher=True)
		return user 



class Custom_user(AbstractBaseUser):
	email		=models.EmailField(max_length=255, unique=True)
	name		=models.BooleanField(default=True)
	active		=models.BooleanField(default=False)
	staff		=models.BooleanField(default=False)
	student		=models.BooleanField(default=False)
	teacher		=models.BooleanField(default=False)
	admin		=models.BooleanField(default=False)
	timestamp	=models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD 	= 'email'

	REQUIRED_FIELDS	= []

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.email

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_student(self):
		return self.student

	@property
	def is_teacher(self):
		return self.teacher

	@property
	def is_active(self):
		return self.active
 
		
	

	
	







