from django.contrib import admin
from django.urls import path, include
from .views import home,signup,secret_page

urlpatterns = [
	path('',home ,name='home'),
    path('secrate', secret_page),
	path('signup',signup ,name='signup'),
]