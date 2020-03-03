from django.contrib import admin
from django.urls import path, include
from .views import home,signup,secret_page,loggedin

urlpatterns = [
	path('',home ,name='home'),
    path('secrate', secret_page),
	path('signup',signup ,name='signup'),
	path('welcome',loggedin,name='welcome')
]