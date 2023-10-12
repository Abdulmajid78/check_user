# users/views.py

from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')  # Redirect to login page or a thank you page
    else:
        form = RegistrationForm()
    return render(request, 'auth/sign-up.html', {'form': form})
