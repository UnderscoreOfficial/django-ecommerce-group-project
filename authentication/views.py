from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout as logout_user

from .forms import RegisterForm, LoginForm

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login_user(request, user)
            return redirect('homepage')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'authentication/register.html', context)

def login(request):
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        user = authenticate(request, 
                            username=request.POST.get('username'), 
                            password=request.POST.get('password'))
        
        if user is None:
            context = {
                'form': form,
                'error': 'Invalid username of password'}
            return render(request, 'authentication/login.html', context) 
         
        login_user(request, user)
        return redirect('homepage')

    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'authentication/login.html', context)

def logout(request):
    logout_user(request)
    return redirect('login')