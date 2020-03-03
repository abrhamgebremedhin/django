from django import forms

from.models import product

class ProductForm(forms.ModelForm):
	class Meta:
		model=product
		fields = [
			'title',
			'description',
			'price'
		]

class ProductForm2(forms.Form):
	title	=forms.CharField()
	description=forms.CharField()
	price	=forms.DecimalField()
	
	def clean_title(self,*args,**kwargs):
		title = self.cleaned_data.get('title')
		if not 'SF-' in title:
			raise forms.ValidationError("haha u suck")
		else:
			print("done")
		