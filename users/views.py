from django.shortcuts import render
from django.views.generic import TemplateView


class CandidatesView(TemplateView):
    template_name = 'candidate.html'


class CandidateDetailsView(TemplateView):
    template_name = 'candidate-details.html'


class SignInView(TemplateView):
    template_name = 'sign-in.html'


class SignUpView(TemplateView):
    template_name = 'sign-up.html'