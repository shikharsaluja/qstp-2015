
from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
	return render(request,"suneha/homepage.html")
def Page1(request):
	return render(request,"suneha/page1.html")
# Create your views here.
