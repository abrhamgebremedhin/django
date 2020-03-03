from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
    is_intern = models.BooleanField(default=False)
    is_HR = models.BooleanField(default=False)

class InternProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='intern_profile')
	bio = models.CharField(max_length=30, blank=True)
	location = models.CharField(max_length=30, blank=True)
  
class HRProfile(models.Model):
  	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='hr_profile')
  	company_name = models.CharField(max_length=100, blank=True)
  	website = models.CharField(max_length=100, blank=True)
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_intern:
		InternProfile.objects.get_or_create(user = instance)
	else:
		HRProfile.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_intern:
		instance.intern_profile.save()
	else:
		HRProfile.objects.get_or_create(user = instance)