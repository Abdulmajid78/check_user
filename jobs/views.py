from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, DetailView
from users.models import EmployeeModel

from .forms import CommentForm
from .models import Comment


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


class EmployeeDetailsView(DetailView):
    model = EmployeeModel
    template_name = 'employee-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        form = CommentForm()
        employee = get_object_or_404(EmployeeModel, pk=pk)
        comments = employee.comment_set.all()

        context['employee'] = employee
        context['comments'] = comments
        context['form'] = form

        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = EmployeeModel.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            user = request.user
            if user.is_authenticated and not user.is_individual:
                name = form.cleaned_data['name']
                position = form.cleaned_data['position']
                employ_from = form.cleaned_data['employ_from']
                employ_to = form.cleaned_data['employ_to']
                content = form.cleaned_data['content']

                comment = Comment.objects.create(
                    name=name, position=position, employ_from=employ_from, employ_to=employ_to, content=content, post=post
                )

                form = CommentForm()
                context['form'] = form
                return self.render_to_response(context=context)

        return self.render_to_response(context=context)


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
