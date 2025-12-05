from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as account_login
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conform_password = request.POST['conform_password']
        if password == conform_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('home')
        else:
            return render(request,'register.html',{'passmatch':False})
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            account_login(request,user)
            messages.success(request, f"New account created: {username}")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    return redirect('home')