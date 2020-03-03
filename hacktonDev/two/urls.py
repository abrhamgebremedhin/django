from django.contrib import admin
from django.urls import path, include
from .views import home,signup,secret_page,loggedin,update_profile,Edit_articel,editTest,List,Add_Blood,searchUser,searchBlood,BookStorage,searchRequest

urlpatterns = [
	path('',home ,name='home'),
	path('signup',signup ,name='signup'),
	path('welcome',loggedin,name='welcome'),
	path('profile',update_profile ,name='_profile'),
	path('Book/<int:id>',BookStorage,name='book'),
	path('List',List,name='list'),
	path('addb',Add_Blood,name='addBlood'),
	path('searchUser', searchUser, name='search1'),
	path('searchBlood',searchBlood,name='search2'),
	path('searchRequested',searchRequest,name='search3'),

]