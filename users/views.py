from django.shortcuts import render
from django.views.generic import TemplateView


class SignInView(TemplateView):
    template_name = 'sign-in.html'


class SignUpView(TemplateView):
    template_name = 'sign-up.html'


class AccountView(TemplateView):
    template_name = 'account.html'


class ResetPasswordView(TemplateView):
    template_name = 'reset-password.html'
