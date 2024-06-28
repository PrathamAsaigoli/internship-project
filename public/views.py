from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from . import models

@csrf_exempt  # Disable CSRF validation for testing purposes, be cautious with this in production
def signup_user(request):
    if request.method == "POST":
           
            Name = request.POST['name']
            Email = request.POST['email']
            Password = request.POST['password']
            if models.Signup.objects.filter(name=Name,email=Email).exists():
                  messages.error(request, "Username already exist")

            else:
                  data = models.Signup(name=Name, email=Email, password=Password)
                  data.save()
                  # messages.success(request, 'Account created successfully')
                  return redirect('login')     
    return render(request,"signup.html")


@csrf_exempt
def login_user(request):
      if request.method == "POST":
            
            email = request.POST['email']
            password = request.POST['password']
            # user = authenticate(request, email=email, password=password)
            if models.Signup.objects.filter(email=email,password=password).exists():
                  data = models.Login(email=email, password=email)
                  data.save()
                  return redirect('products')   
            else:
                  messages.error(request,'Account does no exist')

           
                            
      return render(request,"login.html")



