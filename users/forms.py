from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UserRegistrationForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = CompanyUser
        fields = ('username', 'profile_picture', 'password', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CompanyUser
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['company_name', 'about', 'city', 'address', 'year_of_establishment', 'photo']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id) \
            .filter(email=data)
        if qs.exists():
            raise forms.ValidationError(' Email already in use.')
        return data

########## up

# class CompanyProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['company_name', 'about', 'city', 'address', 'year_of_establishment']


# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password1', 'password2')


# class IndividualUserRegistrationForm(UserCreationForm):
#     class Meta:
#         model = IndividualUser
#         fields = ('username', 'password1', 'password2')


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['name', 'email', 'phone']

#


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = ProfileModel
#         fields = ['company_name', 'about', 'address', 'year_of_establishment']
