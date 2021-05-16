from django.shortcuts import render,redirect
from django.http import HttpResponse
from web.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,"web/index.html")
def follow(request):
	return render(request,"web/followus.html")
def contact(request):
	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		desc=request.POST.get('desc')
		contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
		contact.save()
		messages.success(request, 'Your message has been sent!')

	return render(request,'web/contact.html')