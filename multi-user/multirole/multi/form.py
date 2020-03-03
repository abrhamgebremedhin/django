from django import forms
from .models import User,InternProfile,HRProfile

class UserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ('is_intern','is_HR')

class InternProfileForm(forms.ModelForm):
    class Meta:
        model = InternProfile
        fields = ('location', 'bio')
        
class HRProfileForm(forms.ModelForm):
    class Meta:
        model = HRProfile
        fields = ('company_name', 'website')

class Userdata(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email',)