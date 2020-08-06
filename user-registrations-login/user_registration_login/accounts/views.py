from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from accounts.forms import UserRegisterForm, LoginForm


def register(request, template="accounts/register.html"):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			user = User(username=username, email=email,
						first_name=first_name)
			user.set_password(password)
			user.is_active = False
			user.save()
			return HttpResponseRedirect('/login')
	else:
		form = UserRegisterForm()        
	return render(request, template, context)
