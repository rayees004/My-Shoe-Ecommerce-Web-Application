

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as account_login
from django.contrib import messages
from rest_framework import status
from .serializers import ResendOtpSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
# Create your views here.

from django.core.mail import send_mail

def send_otp_email(email, otp):
    send_mail(
        subject='Your OTP Code',
        message=f'Your OTP is {otp}',
        from_email='mrc53445@gmail.com',
        recipient_list=[email],
        fail_silently=False,
    )


 
def verify_otp(request):
    if request.method == 'POST':
       user_otp = request.POST['otp']
       try:
            otp = request.session['otp']
       except:
           otp = ""
           redirect('register')
       print("saved otp",(otp))
       print("user sended otp",(user_otp))
       if str(otp) == user_otp:
           username = request.session['username']
           email = request.session['email']
           password = request.session['password']
           User.objects.create_user(username=username,email=email,password=password)
           return redirect("home")
    return render(request,'verify_otp.html')
    

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conform_password = request.POST['conform_password']
        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'userexists':True})
        if password == conform_password:
            request.session['username'] = username
            request.session['email'] = email
            request.session['password'] = password
           
            # otp generation
            otp = random.randint(100000,999999)
            request.session['otp'] = otp
            send_otp_email(email,otp)

            return redirect('verify_otp')
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
            request.session['loginerror'] = ""
            return redirect('home')
        else:
            request.session['loginerror'] = "username or password desnot match"
        
    return redirect('home')
    # return render(request,"login.html")