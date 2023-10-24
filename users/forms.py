
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

from django.contrib.auth.forms import UserCreationForm


class IndividualUserRegistrationForm(UserCreationForm):
    class Meta:
        model = IndividualUser
        fields = ('username', 'password1', 'password2')


class CompanyUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CompanyUser
        fields = ('username', 'company_name', 'password1', 'password2')


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'address', 'year_of_establishment']


########### down


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

########## up


from django import forms
from .models import EmployeeModel


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ('first_name', 'last_name', 'third_name', 'phone_number', 'born_city', 'current_city')


