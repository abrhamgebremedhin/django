from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from .form import ArticleForm
from datetime import date 
from django.contrib.auth.decorators import login_required

# Create your views here.  

@login_required 
def Add_articel(request):
	form=ArticleForm(request.POST or None)
	if request.method =='POST':
		form=ArticleForm(request.POST)
		if form.is_valid():
			title =request.POST.get('title')
			content =request.POST.get('content')
			d =date.today()
			publish =request.POST.get('publish')
			#print("****************************")
			#print(publish)
			if publish == None:
				publish =False
			else:
				publish =True
			Article.objects.create(title=title,content=content,date=d,publish=publish)
			return redirect('list')
	context={'form':form}
	return render(request,"article_edit.html",context)

def Show_articel(request,id):
	obj=Article.objects.get(id=id)
	obj=get_object_or_404(Article,id=id)
	context={'obj':obj}
	return render(request,"article_show.html",context)
	'''
	def product_dinamic_view(request,id):
	#obj=product.objects.get(id=id)
	obj=get_object_or_404(product,id=id)
	context={'obj':obj}
	return render(request,"product/dynamic.html",context)
	'''

@login_required
def Edit_articel(request,id):
	data=get_object_or_404(Article,id=id)
	form=ArticleForm(request.POST or None,instance=data) 
	context={'form':form}
	if request.POST:
		if form.is_valid():
			form.save()
			return redirect('list')
	return render(request,"article_edit.html",context)
@login_required
def delete_articel(request,id):
	obj=get_object_or_404(Article,id=id)
	if request.method=='POST':
		obj.delete() 
		return redirect('list')
	context={'obj':obj}
	return render(request,"article_delete.html",context)


def Published_articels_list(request):
	obj=Article.objects.all()
	i=1 
	li = []
	num=obj.count()
	for art in obj:
		if art.publish:	
			#print(art.publish)
			li.insert(i, art)
		i=i+1

	context={'obj':li}
	return render(request,"article_list.html",context)

@login_required
def Unpublished_article_list(request):
	obj=Article.objects.all()
	i=1 
	li = []
	num=obj.count()
	for art in obj:
		if not art.publish:	
			#print(art.publish)
			li.insert(i, art)
		i=i+1

	context={'obj':li}
	return render(request,"article_list.html",context)



