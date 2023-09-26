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


class FindJobView(TemplateView):
    template_name = 'find-job.html'


class JobListView(TemplateView):
    template_name = 'job-list.html'


class PostJobView(TemplateView):
    template_name = 'post-job.html'


class JobDetailView(TemplateView):
    template_name = 'job-details.html'


class AccountView(TemplateView):
    template_name = 'account.html'


class ResumeView(TemplateView):
    template_name = 'resume.html'
