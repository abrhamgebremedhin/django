from django.shortcuts import render,redirect
from .models import Post
from .form import PostForm
from datetime import date 
from django.contrib.auth.decorators import login_required

# Create your views here.
def viewPost(request):
	obj=Post.objects.all()
	context={'obj':obj}
	return render(request,"list.html",context)
	
@login_required 
def postinfo(request):
	form=PostForm(request.POST or None)
	if request.method =='POST':
		form=PostForm(request.POST)
		if form.is_valid():

			title =request.POST.get('title')
			content =request.POST.get('body')
			d =date.today()
			audience = request.POST.get('audience')
			postedBy = request.user

			Post.objects.create(title=title,body=content,Date=d,audience=audience,postedBy=postedBy)
			return redirect('post')
	context={'form':form}
	return render(request,"Postform.html",context)
