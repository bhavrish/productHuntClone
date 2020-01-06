from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	if request.method== 'POST':
		if request.POST['password1']==request.POST['password2']: # if passwords match
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'signup.html', {'error':'Username has already been taken'}) # pass error message as dict
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
				auth.login(request,user)
				return redirect('home') # redirects to home page
		else:
			return render(request, 'signup.html', {'error':'Passwords must match'}) # pass error message as dict
	else:
		return render(request, 'signup.html')

def login(request):
	if request.method== 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None: # if user exists
			auth.login(request,user)
			return redirect('home') # redirects to home page
		else:
			return render(request, 'login.html', {'error':'Username or password is incorrect'}) # pass error message as dict
	else:
		return render(request, 'login.html')

def logout(request):
	if request.method== 'POST':
		auth.logout(request)
		return redirect('home') # redirects to home page