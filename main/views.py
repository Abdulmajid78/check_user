from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class CandidatesView(TemplateView):
    template_name = 'candidate.html'

class CandidateDetailsView(TemplateView):
    template_name = 'candidate-details.html'
