from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import random, seed
from datetime import date

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender         =models.CharField(max_length=120)
    donations     =models.DecimalField(decimal_places=2, max_digits=10000,default=0)
    requests    =models.DecimalField(decimal_places=2, max_digits=10000,default=0)
    bloodtype    =models.CharField(max_length=120,blank=True)
    uniq_id        =models.CharField(max_length=120,blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        email=instance.email
        Profile.uniq_id=uniq_id(email)
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
def uniq_id(email):
    ran=randnum()
    uniq_id=email[:3]+randD()+str(int(randnum()))
    return uniq_id

def randnum():
    seed(1)
    value = random()
    return value*1000

def randD():
    time = date.today().strftime("%H")
    return time
    
class Storage(models.Model):
    bloodType        =models.CharField(max_length=120)
    storgeArea        =models.CharField(max_length=120,blank=False,null=False)
    dateOfStorage    =models.DateField()#pub_date=date.today()
    donatedBy        =models.ForeignKey(User, on_delete=models.CASCADE,related_name='donator')
    booked            =models.BooleanField(default=False,null=True,blank=True)

class Request(models.Model):
    RequestedBlood  =models.ForeignKey(Storage, on_delete=models.CASCADE)
    bookedBy        =models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,related_name='reciver')


