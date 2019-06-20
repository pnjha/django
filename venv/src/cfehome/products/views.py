from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def product_create_form(request,*args,**kwargs):

	my_form = RawProductForm()

	if request.method == "POST":
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			product_obj = Product.objects.create(**my_form.cleaned_data) 
		else:
			print(my_form.errors)

	context = {
		"form": my_form
	}

	return render(request,"create_product.html",context)

# def product_create_form(request,*args,**kwargs):
	
# 	product_obj = "No data"

# 	if request.method == "POST":
# 		title = request.POST.get('title')
# 		description = request.POST.get('description')
# 		price = request.POST.get('price')
# 		summary = request.POST.get('summary')
# 		manufacturer = request.POST.get('manufacturer')

# 		try:
# 			if title is not None or description is not None or price is not None or manufacturer is not None or summary is not None:
# 				product_obj = Product.objects.create(title = title,manufacturer = manufacturer,summary = summary,price = price,description = description)
# 		except:
# 			product_obj = None


# 	context = {
# 		"product_obj":product_obj 
# 	}

# 	return render(request,"create_product.html",context)

# def product_create_form(request,*args,**kwargs):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ProductForm()

# 	context = {
# 		"form" : form
# 	}

# 	context = {}

# 	return render(request,"create_product.html",context)


def product_detail_view(request,*args,**kwargs):
	obj = Product.objects.get(id=1)
	# context = {
	# 	"title" : obj.title,
	# 	'description': obj.description
	# }

	context = {
		"object" : obj
	}
	return render(request,"detail.html",context)