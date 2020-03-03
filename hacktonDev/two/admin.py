from django.contrib import admin
from .models import Profile,Request,Storage

admin.site.register(Profile)
admin.site.register(Storage)
admin.site.register(Request)