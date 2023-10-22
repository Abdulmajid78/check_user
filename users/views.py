from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm, CompanyProfileForm

from django.shortcuts import render, redirect
from .forms import IndividualUserRegistrationForm, CompanyUserRegistrationForm, EmployeeModelForm

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import CompanyProfile

from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import CompanyProfile
from .forms import CompanyProfileForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class CompanyProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = 'profile-change.html'
    success_url = reverse_lazy('main:home')  # Redirect to the desired page after update


def register_individual(request):
    if request.method == "POST":
        form = IndividualUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')  # Redirect to the desired page
    else:
        form = IndividualUserRegistrationForm()
    return render(request, 'auth/sign-up.html', {'form': form})


def register_company(request):
    if request.method == "POST":
        form = CompanyUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')  # Redirect to the desired page
    else:
        form = CompanyUserRegistrationForm()
    return render(request, 'auth/sign-up-company.html', {'form': form})


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


def logout_view(request):
    logout(request)
    return redirect('main:home')


def add_employee(request):
    if request.method == "POST":
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('main:home')  # Редирект на желаемую страницу после успешного добавления
    else:
        form = EmployeeModelForm()
    return render(request, 'jobs/post-employee.html', {'form': form})




