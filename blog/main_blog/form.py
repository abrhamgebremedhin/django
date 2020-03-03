from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
		class Meta:
			model=Article
			fields = [
				'title',
				'content',
				'publish'

			]


class ArticleForm2(forms.Form):
	title	=forms.CharField()
	content	=forms.CharField()
	price	=forms.DecimalField()