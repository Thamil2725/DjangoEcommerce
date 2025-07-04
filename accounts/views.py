from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User


# Create your views here.

def show_register(request):
    return render(request, 'register.html')


def user_register(request):
        username = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return render(request, 'register.html')
    
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request, 'register.html')
        
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password didn\'t Match')
            return render(request, 'register.html')


def show_login(request):

    return render(request, 'login.html')


def user_login(request):
        
        username = request.POST['userid']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Wrong Credentials')
            return redirect('login')


def logout(request):
     auth.logout(request)
     return redirect('/')
