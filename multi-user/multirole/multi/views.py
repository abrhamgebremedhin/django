from django.shortcuts import render,redirect
from .form import UserForm,Userdata,InternProfileForm,HRProfileForm
from .models import User,InternProfile,HRProfile
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registor(request):
    user_form = UserForm()
    if request.method == 'POST':
        x=request.POST.get('is_intern')
        if x == "on":
            return redirect('two')
        else:
            return redirect('three')
    return render(request, 'registor.html',{'user_form': user_form})

def intern_profile_view(request):
    user_form = Userdata()
    profile_form = InternProfileForm()
    if request.method == 'POST':
     user_form = Userdata(request.POST)
     profile_form = InternProfileForm(request.POST)
     if user_form.is_valid() and profile_form.is_valid():#user = user_form.save(commit=False)
            user_form.is_intern =True
            user_form.save()
            profile_form.user=user_form
            print("-------------")
            print(profile_form.user)
            profile_form.save()
            user_form = Userdata()
            profile_form = InternProfileForm()
    
    return render(request, 'intern_profile.html',{'user_form':user_form,'profile_form':profile_form})


def HR_view(request):
    user_form = Userdata()
    profile_form = HRProfileForm()
    if request.method == 'POST':
       user_form = Userdata(request.POST)
       profile_form = HRProfileForm(request.POST)
       if user_form.is_valid() and profile_form.is_valid():#user = user_form.save(commit=False)
            user_form.is_HR =True
            user_form.save()
            profile_form.user=user_form
            print("-------------")
            print(profile_form.user)
            profile_form.save()
            return redirect('login')
    
    return render(request, 'HR.html',{'user_form':user_form,'profile_form':profile_form})

'''def login_hr(request):
  loginform = loginform()
  if request.method == 'POST':
    loginform = loginform(request.POST)
    unknown = User.objects.all()
    unknown_user = request.POST.get('username')
    for Userslist in unknown:
      if Userslist.username == unknown_user:
        if Userslist.is_HR: '''

