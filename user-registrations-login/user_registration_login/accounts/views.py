from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from accounts.forms import UserRegisterForm, LoginForm


