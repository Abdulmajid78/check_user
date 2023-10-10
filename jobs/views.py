from django.shortcuts import reverse
from django.views.generic import TemplateView, ListView, DeleteView, CreateView
from users.models import EmployeeModel
from django.db.models import Q

from django.shortcuts import get_object_or_404
from .forms import CommentForm


class FindEmployeeView(ListView):
    template_name = 'find-employee.html'

    paginate_by = 14

    def get_queryset(self):
        qs = EmployeeModel.objects.filter(is_active=True)

        search_name = self.request.GET.get('search_name')
        if search_name:
            qs = qs.filter(Q(first_name__icontains=search_name) | Q(last_name__icontains=search_name))

        search_surname = self.request.GET.get('search_surname')
        if search_surname:
            qs = qs.filter(Q(first_name__icontains=search_surname) | Q(last_name__icontains=search_surname))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['employees'] = EmployeeModel.objects.all()
        return data


class EmployeeDetailsView(DeleteView):
    model = EmployeeModel
    template_name = 'employee-details.html'













class JobListView(TemplateView):
    template_name = 'job-list.html'


class ResumeView(TemplateView):
    template_name = 'resume.html'


class JobDetailView(TemplateView):
    template_name = 'job-details.html'


class CandidatesView(TemplateView):
    template_name = 'candidate.html'


class PostJobView(TemplateView):
    template_name = 'post-job.html'