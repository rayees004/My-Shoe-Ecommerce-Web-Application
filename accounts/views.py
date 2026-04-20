

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as account_login
from django.contrib import messages
from rest_framework import status
from .serializers import ResendOtpSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
def resend_otp(request):
    if request.method == 'POST':
        serializer = ResendOtpSerializer(data=request.POST)
        session_id = request.POST.get('session_id')
        # Implement logic to resend OTP using the session_id
        # For example, you can generate a new OTP and send it to the user's email or phone number
        # You can also return a response indicating that the OTP has been resent successfully
        return Response("resend otp success",status=status.HTTP_200_OK)  # Redirect to the OTP verification page after resending the OTP

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
            return render(request,'registerotp.html',{'session_id':request.session.session_key})
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