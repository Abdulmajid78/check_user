from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm, \
    UserEditForm, ProfileEditForm


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile yangilandi ' 'successfully')
        else:
            messages.error(request, 'Hato profile yangilashda')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    return render(request,
                  'account/profile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создать новый объект пользователя,
            # но пока не сохранять его
            new_user = user_form.save(commit=False)
            # Установить выбранный пароль
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохранить объект User
            new_user.save()
            # Создать профиль пользователя
            Profile.objects.create(user=new_user)
            return redirect('main:home')
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


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
    return render(request, 'account/sign-in.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main:home')


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

# def register_company(request):
#     if request.method == "POST":
#         form = CompanyUserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_individual = False  # Устанавливаем is_individual в False для компаний
#             user.save()
#             login(request, user)  # Log in the user immediately after registration
#             return redirect('main:home')  # Redirect to the desired page
#     else:
#         form = CompanyUserRegistrationForm()
#     return render(request, 'auth/sign-up-company.html', {'form': form})


# @login_required
# def company_profile_view(request):
#     company_profile, created = Profile.objects.get_or_create(user=request.user)
#
#     if request.method == 'POST':
#         form = CompanyProfileForm(request.POST, instance=company_profile)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CompanyProfileForm(instance=company_profile)
#
#     return render(request, 'auth/company-account.html', {'form': form})


# def register_individual(request):
#     if request.method == "POST":
#         form = IndividualUserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log in the user immediately after registration
#             return redirect('main:home')  # Redirect to the desired page
#     else:
#         form = IndividualUserRegistrationForm()
#     return render(request, 'auth/sign-up.html', {'form': form})


# Пока обычные пользователи не имеют профиля
# @login_required
# def user_profile_view(request):
#     user_profile = UserProfile.objects.get(user=request.user)
#
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserProfileForm(instance=user_profile)
#
#     return render(request, 'auth/user-account.html', {'form': form})


# class CompanyProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = ProfileModel
#     form_class = CompanyProfileForm
#     template_name = 'profile-change.html'
#     success_url = reverse_lazy('main:home')  # Redirect to the desired page after update


# @login_required
# def profile_view(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ProfileForm(instance=request.user)
#
#     return render(request, 'auth/account.html', {'form': form})
