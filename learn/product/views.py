from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse

from .form import ProductForm,ProductForm2
from .models import product
# Create your views here.

def home(request,*args,**kwargs):
	obj = product.objects.get(id=3)
	test={"var1":"one","var2":"two","var3":[0,1,2,3,4,5],'obj':obj}
	return render(request,"product/home.html",test)

def product_all(request):
	obj=product.objects.all()
	context={'obj':obj}
	return render(request,"product/all.html",context)

def product_form_view(request):
	if request.method == "POST":
		my_new_title = request.POST.get('title')
		price =request.POST.get('price') 
		print(my_new_title)
		product.objects.create(title=my_new_title,price=price,featured=True)
		
	context = {}
	return  render(request, "product/form1.html",context)

def product_dinamic_view(request,id):
	#obj=product.objects.get(id=id)
	obj=get_object_or_404(product,id=id)
	context={'obj':obj}
	return render(request,"product/dynamic.html",context)

def product_delete_view(request,id): 
	obj=get_object_or_404(product,id=id)
	if request.method=='POST':
		obj.delete() 
		return redirect('../../')
	context={'obj':obj}
	return render(request,"product/delete.html",context)


def product_form2_view(request):
	form=ProductForm2(request.POST or None)
	if request.method == "POST":
		form=ProductForm2(request.POST)
		if form.is_valid():
		 	product.objects.create(**form.cleaned_data)
		 	form=ProductForm2()

	context = {'form':form}
	return  render(request, "product/form2.html",context)

def product_form_update(request,id):
	#initial_data = {'title':"this is good"}

	data=get_object_or_404(product,id=id)
	print(data.title)
	form=ProductForm(request.POST or None,instance=data) 
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('../../')
	context = {'form':form}
	return  render(request, "product/update.html",context)

# def product_form_view(request):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ProductForm()

# 	context = {
# 		'object':form
# 	}
# 	return  render(request, "product/form1.html",context)
def product_create_view(request):
	obj = product.objects.get(id=3)
	
	context = {
		'obj':obj
	}
	return  render(request, "product/home.html",context)
