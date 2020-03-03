from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url

from .forms import LoginForm,RegisterForm

def register_page(request):
	form = RegisterForm(request.POST or None)
	context = { "form":form}
	if form.is_valid():
		form.save()
		return redirect('login')
	return render(request,"accounts/register.html",context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form":form
	}
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, "cool.html",context)
		else:
			print("Error")
	return render(request, "accounts/login.html",context)

def logout_view(request):
    logout(request)
    context = {}
    return render(request, "done.html",context)


def profile_view(request):
    context = {}
    return render(request, "profile.html",context)





