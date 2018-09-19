from django.shortcuts import render,redirect

# Create your views here.

def home(request):
	return render(request,'home.html',{})

def add_address(request):
	return render(request,'add_address.html',{})