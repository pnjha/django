from django import forms

from .models import Product

class RawProductForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField(widget=forms.Textarea())
	price = forms.DecimalField()
	summary = forms.CharField()
	manufacturer = forms.CharField()
	email = forms.EmailField()

	def clean_email(self,*args,**kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("Not a valid email")
		return email

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]