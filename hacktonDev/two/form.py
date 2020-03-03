from django import forms
from .models import Profile,User,Storage,Request

class RequestForm(forms.Form):
    """docstring for RequestForm"""
    RequestedBlood   =forms.CharField()
    bookedBy =forms.CharField()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class DateInput(forms.DateInput):
    input_type = 'date'

class A(forms.TextInput):
    input_type = 'hidden'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'location', 'gender','bloodtype','uniq_id') 
        Place_CHOICES = (
                ('AddisAbaba', 'AddisAbaba'), 
                ('adama', 'adama'),
                ('hawasa', 'hawasa'),
               
                )
        bloodtype =(('A-','A-'),('A+','A+'),('B+','B+'),('B-','B-'),('o+','o+'),('o-','o-'),('ab+','ab+'),('ab-','ab-'))
        
        gender = (('male','male'),('female','female'))

        widgets = {
            'birth_date': DateInput(),
            'uniq_id': A,
            'location': forms.Select(choices=Place_CHOICES),
            'bloodtype': forms.Select(choices=bloodtype),
            'gender': forms.Select(choices=gender),
        }
        

class Profle2(forms.ModelForm):
    birth_date    =forms.DateField(widget=DateInput)
    location     =forms.CharField()
    gender         =forms.CharField()
    bloodtype    =forms.CharField()

class StoreAdd(forms.ModelForm):
    
    class Meta:

        model = Storage
        fields = ('dateOfStorage', 'storgeArea', 'donatedBy','bloodType','booked') 
        AGE_CHOICES = (
                ('AddisAbaba', 'addis ababa'), #First one is the value of select option and second is the displayed value in option
                ('adama', 'adama'),
                ('hawasa', 'hawasa'),
               
                )
        bloodtype =(('A-','A-'),('A+','A+'),('B+','B+'),('B-','B-'),('o+','o+'),('o-','o-'),('ab+','ab+'),('ab-','ab-'))
        
        widgets = {
                'dateOfStorage': DateInput(),
                'storgeArea': forms.Select(choices=AGE_CHOICES),
                'bloodType': forms.Select(choices=bloodtype),
                'booked': A,
            }



       
        
    



       