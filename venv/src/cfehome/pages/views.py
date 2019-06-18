from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	# return HttpResponse("<h1>Hello World</h1>") 
	data = {
	"username" : 'Prakash Nath Jha',
	"gender" : "Male",
	"my_list" : [10,20,30],
	"html_text": "<h2>Prakash</h2>"
	}
	return render(request,"home.html",data)