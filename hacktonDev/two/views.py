from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .form import ProfileForm,Profle2,UserForm,StoreAdd,RequestForm
from .models import Profile,User,Storage,Request
from .filters import UserFilter,BloodFilter,RequestFilter

@login_required
def BookStorage(request,id):
    obj=Storage.objects.get(id=id)
    context={'obj':obj}
    if request.method == 'POST':
        store = StoreAdd(request.POST)
    if request.method == "POST":
        x = request.user
        y=Storage.objects.get(id=id)
        #print("one")
        y.booked=True
        #print("two") 
        y.save()
        #print("three")
        #instance.booked=True
        #instance.save        
        Request.objects.create(bookedBy=x,RequestedBlood=y)
        #print("done")
        return redirect('search2')
    return render(request,"bookB.html",context)

@login_required
def requestList(request):
    form=Request.objects.all()
    return render(request,'RequestView.html',{'form':form})

@login_required
def searchUser(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search.html', {'filter': user_filter})

@login_required
def searchRequest(request):
    user_list = Request.objects.all()
    user_filter = RequestFilter(request.GET, queryset=user_list)
    return render(request, 'RequestView.html', {'filter': user_filter})

def home(request):
    print("+++++++")
    print(request.user)
    
    if request.user.is_authenticated:
        req=User.objects.get(id=request.user.id)
        context={'donations':request.user.profile.donations,'request':req}
    else:
        context={}
    return render(request,'cool.html',context)

@login_required
def searchBlood(request):
    user_list = Storage.objects.all()
    print(user_list.count())
    user_filter = BloodFilter(request.GET, queryset=user_list)
    return render(request, 'searchBlood.html', {'filter': user_filter})

@login_required
def update_profile(request):
    if request.method == 'POST':
        print("hi--")
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            print("hi--")
            user_form.save()
            profile_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('home')
        
    else:
        x=request.user.id
        data = User.objects.get(pk=x)
        user_form = UserForm(instance=data)
        profile_form = ProfileForm(instance=data.profile)
    return render(request, 'edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def Edit_articel(request, id):
    user = User.objects.get(pk=id)
    context = {'user': user}

    return render(request, 'show.html',context )    

@login_required
def editTest(request):
    x=request.user.id
    user = User.objects.get(id=x)
    context = {'user': user}
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        user_form = UserForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('home')
    return render(request, 'edit.html',context )



def signup(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			#user:hello #pass:pass1wdisgood
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request,'registration/signup.html',{
		'form':form
		})


@login_required
def secret_page(request):
	return render(request,'secret_page.html')

def loggedin(request):
    context={}
    return render(request,'welcome.html',context)

def List(request):
    user=Storage.objects.all()
    context={'users':user}
    return render(request,'list_all.html',context)

def Add_Blood(request):
    new=StoreAdd(request.POST or None)
    context={'new':new}
    if request.method == 'POST':
        if new.is_valid():
            new.save()
            return redirect('home')
    return render(request,'add_blood.html',context)




