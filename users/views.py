from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    '''
    View function for the signup page.
    Allows users to register using a sign up form.
    '''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    '''
    View function for the login page.
    Allows users to log in to their account.
    '''

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    '''
    View function to log out the user.
    '''

    logout(request)
    return redirect('home')
