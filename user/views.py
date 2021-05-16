from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
	if request.method=="POST":
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Your Account Has Been Created! You Can Now LogIn')
			return redirect('login')
	else:
		form=UserRegisterForm()

	return render(request,"user/register.html",{"form":form})

def shop(request):
	return render(request,"web/shop.html")
def profile(request):
	return render(request,"user/profile.html")
@login_required
def buy(request):
	messages.success(request,f'Order Placed Successfully!!!!')
	# messages.success(request,f"Don't Want To Buy More Then Please Logout Successfully" )
	return redirect('shop')