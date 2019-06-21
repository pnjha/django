from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

# def product_create_form(request,*args,**kwargs):

# 	initial_data = {
# 		'title' : "random"
# 	}

# 	my_form = RawProductForm(initial=initial_data)

# 	if request.method == "POST":
# 		my_form = RawProductForm(request.POST or None)
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			product_obj = Product.objects.create(**my_form.cleaned_data) 
# 		else:
# 			print(my_form.errors)

# 	context = {
# 		"form": my_form
# 	}

# 	return render(request,"create_product.html",context)

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

def product_create_form(request,*args,**kwargs):

	initial_data = {
		'title': "prakash"
	}

	obj = Product.objects.get(id=16)
	form = ProductForm(request.POST or None,initial=initial_data,instance=obj)

	if request.method == "POST":
		if form.is_valid():
			form.save()
			form = ProductForm()

	context = {
		"form" : form
	}

	return render(request,"create_product.html",context)


def product_detail_view(request,my_id,*args,**kwargs):
	# obj = Product.objects.get(id=my_id)
	# obj = get_object_or_404(Product,id=my_id)
	
	try:
		obj = Product.objects.get(id=my_id)
	except:
		raise Http404

	# context = {
	# 	"title" : obj.title,
	# 	'description': obj.description
	# }

	context = {
		"object" : obj
	}
	return render(request,"detail.html",context)

def product_delete_view(request,my_id):
	
	obj = get_object_or_404(Product,id=my_id)
	
	if request.method == "POST":
		obj.delete()
		return redirect("../1")

	context = {
		"object" : obj
	}
	return render(request,"delete_product.html",context)

def product_list_view(request):
	
	queryset = Product.objects.all()
	
	context = {
		"object_list" : queryset
	}
	return render(request,"product_list.html",context)