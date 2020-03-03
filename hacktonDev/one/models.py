from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from random import random, seed
from datetime import datetime


class UserManager(BaseUserManager):
    def create_user(self, name,email,gender ,donations,requests,bloodtype, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("user must have a password")

        user_obj =self.model(
            email = self.normalize_email(email)
            )
        user_obj.set_password(password)
        user_obj.gender = gender()
        user_obj.donations = donations()
        user_obj.requests=requests()
        user_obj.bloodtype=bloodtype()
        user_obj.uniq_id=uniq_id()
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

    
# Create your models here.
class User(AbstractUser):
    gender         =models.CharField(max_length=120)
    donations     =models.DecimalField(decimal_places=2, max_digits=10000,default=0)
    requests    =models.DecimalField(decimal_places=2, max_digits=10000,default=0)
    bloodtype    =models.CharField(max_length=120,blank=True)
    email        =models.EmailField(max_length=255, unique=True)
    uniq_id        =models.CharField(max_length=120)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS= []

    objects    = UserManager()

    def __str__(self):
        return self.uniq_id

    def has_perm(self, perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property 
    def gender(self):
        return self.gender

    @property
    def donations(self):
        return self.donations

    @property
    def requests(self):
        return self.requests 

    @property
    def bloodtype(self):
        return self.bloodtype

    @property
    def uniq_id(self):
        email=self.email
        ran=randnum()
        ran=ran*100
        uniq_id=email[:3]+randD()+str(int(randnum()))
        return uniq_id

    @property
    def is_active(self):
        return self.active

    def randnum():
        seed(1)
        value = random()
        return value*1000

    def randD():
        """
        year = now.strftime("%Y")
        print("year:", year)
        month = now.strftime("%m")
        print("month:", month)
        day = now.strftime("%d")
        print("day:", day)
        time = now.strftime("%H:%M:%S")
        """
        time = now.strftime("%H")
        return time

class Storage(models.Model):
    bloodType        =models.CharField(max_length=120)
    storgeArea        =models.CharField(max_length=120,blank=False,null=False)
    dateOfStorage    =models.DateField()#pub_date=date.today()
    donatedBy        =models.ForeignKey(User, on_delete=models.CASCADE,related_name='donator')
    booked            =models.BooleanField(default=False,null=True,blank=True)
    bookedBy        =models.ForeignKey(User, on_delete=models.CASCADE,blank=True,related_name='reciver')
