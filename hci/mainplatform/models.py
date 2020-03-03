from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title		=models.CharField(max_length=120)
	body		=models.TextField(blank=False,null=False)
	Date    	=models.DateField()#pub_date=date.today()
	audience	=models.CharField(max_length=120)
	postedBy	=models.ForeignKey(User, on_delete=models.CASCADE)

