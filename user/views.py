from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages

def register(request):
    return render(request, 'users/register.html')

# class CustomLoginView(LoginView):
#     template_name = 'users/login.html'
#     authentication_form = UserLoginForm

# class CustomLogoutView(LogoutView):
#     template_name = 'users/logout.html'

@login_required
def home(request):
    return render(request,'base.html')  # Replace with your home view

def login(request):
    return render(request,'base.html')  # Replace with your home view

def logout(request):
    return render(request,'base.html')  # Replace with your home view
