from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    ''' Used to login a user'''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("There Was An Error Logging In, \
                Try Again..."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    ''' Used to Register a user'''
    logout(request)
    messages.success(request, ("You have succesfully logged out."))
    return redirect('index')


def register_user(request):
    ''' Used to Register a user'''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have successfully registered"))
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })
