# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')  # Redirect to login page or a thank you page
    else:
        form = RegistrationForm()
    return render(request, 'auth/sign-up.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a specific page after login, e.g., the user's profile
                return redirect('main:home')
            else:
                # Invalid login
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'auth/sign-in.html', {'form': form})
