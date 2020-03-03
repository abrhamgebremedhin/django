from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request,*args,**kwargs):
	##obj =  product.objects.get(id=1)
	test={"var1":"one","var2":"two","var3":[0,1,2,3,4,5]}

	return render(request,"home.html",test)
def about(request,*args,**kwargs):
	return render(request,"about.html",{})
def content(request,*args,**kwargs):
	return render(request,"content.html",{})
def base(request,*args,**kwargs):
	return render(request,"base.html",{})